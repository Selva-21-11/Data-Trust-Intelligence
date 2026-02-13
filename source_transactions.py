import pandas as pd
import numpy as np
from faker import Faker
import random

fake = Faker()
np.random.seed(42)

rows = 30000

data = []

for i in range(rows):
    transaction_id = f"T{i+1:06d}"
    customer_id = f"C{random.randint(1000, 9999)}"
    source_system = random.choice(["Billing", "CRM", "App"])
    metric_name = random.choice(["Revenue", "Orders", "Tickets"])

    # Base value logic
    if metric_name == "Revenue":
        metric_value = round(random.uniform(1000, 20000), 2)
    elif metric_name == "Orders":
        metric_value = random.randint(1, 10)
    else:
        metric_value = random.randint(1, 5)

    transaction_date = fake.date_between(start_date="-12M", end_date="today")

    # Introduce data quality issues
    issue_chance = random.random()
    if issue_chance < 0.05:
        metric_value = None
        record_status = "missing"
    elif issue_chance < 0.10:
        record_status = "duplicate"
    else:
        record_status = "valid"

    data.append([
        transaction_id,
        customer_id,
        source_system,
        metric_name,
        metric_value,
        transaction_date,
        record_status
    ])

df_source = pd.DataFrame(data, columns=[
    "transaction_id", "customer_id", "source_system",
    "metric_name", "metric_value", "transaction_date", "record_status"
])

df_source.to_csv("source_transactions.csv", index=False)

print("source_transactions.csv generated")
