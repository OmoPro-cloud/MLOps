import pandas as pd
import numpy as np

#evidently imports
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset, DataQualityPreset, TargetDriftPreset

#generate reference data
np.random.seed(42)

reference_data = pd.DataFrame({
    "age": np.random.normal(loc=35, scale=10, size=1000),
    "visits_per_month": np.random.normal(loc=12, scale=3, size=1000),
    "monthly_fee": np.random.choice([30, 50], size=1000),
    "churn_target": np.random.choice([0, 1], size=1000, p=[0.95, 0.05])
})

#generate current data
current_data = pd.DataFrame({
    #no drift in demographics
    "age": np.random.normal(loc=35, scale=10, size=1000),

    #major drift: fewer visits
    "visits_per_month": np.random.normal(loc=4, scale=2, size=1000),

    #price increase
    "monthly_fee": np.random.choice([50, 70], size=1000),

    #target drift: churn increased
    "churn_target": np.random.choice([0, 1], size=1000, p=[0.80, 0.20])
})

print("Datasets generated successfully!")

# -----------------------------
# Column Mapping (IMPORTANT)
# -----------------------------
column_mapping = ColumnMapping()
column_mapping.target = "churn_target"

# -----------------------------
# Create Evidently Report
# -----------------------------
report = Report(metrics=[
    DataQualityPreset(),
    DataDriftPreset(),
    TargetDriftPreset()
])

print("Running drift analysis...")

report.run(
    reference_data=reference_data,
    current_data=current_data,
    column_mapping=column_mapping
)

# -----------------------------
# Save report
# -----------------------------
report.save_html("gym_churn_report.html")

print("Report generated: gym_churn_report.html")