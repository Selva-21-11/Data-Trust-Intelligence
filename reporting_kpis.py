import pandas as pd
import random
from faker import Faker

fake = Faker()


reports = []

for _ in range(2000):
    report_id = f"R{random.randint(10000, 99999)}"
    metric_name = random.choice(["Revenue", "Orders", "Tickets"])
    report_owner = random.choice(["Finance", "Sales", "Operations"])

    base_value = random.uniform(50000, 200000)

    # Introduce mismatch
    reported_value = round(base_value * random.uniform(0.95, 1.05), 2)

    report_date = fake.date_between(start_date="-12M", end_date="today")

    reports.append([
        report_id,
        metric_name,
        reported_value,
        report_date,
        report_owner
    ])

df_reports = pd.DataFrame(reports, columns=[
    "report_id", "metric_name", "reported_value", "report_date", "report_owner"
])

df_reports.to_csv("reporting_kpis.csv", index=False)

print("reporting_kpis.csv generated")
