import pandas as pd
import random
from faker import Faker

fake = Faker()


issues = []

for i in range(1000):
    issue_id = f"DQ{i+1:05d}"
    issue_type = random.choice(["missing", "duplicate", "mismatch"])
    affected_metric = random.choice(["Revenue", "Orders", "Tickets"])
    severity = random.choice(["low", "medium", "high"])
    detection_date = fake.date_between(start_date="-12M", end_date="today")

    resolution_hours = random.randint(1, 48)

    issues.append([
        issue_id,
        issue_type,
        affected_metric,
        severity,
        detection_date,
        resolution_hours
    ])

df_issues = pd.DataFrame(issues, columns=[
    "issue_id", "issue_type", "affected_metric",
    "severity", "detection_date", "resolution_hours"
])

df_issues.to_csv("data_quality_issues.csv", index=False)

print("data_quality_issues.csv generated")
