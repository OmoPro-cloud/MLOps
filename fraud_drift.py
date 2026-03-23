import pandas as pd
import numpy as np

import evidently
print("Evidently version: ", evidently._version)
#generate REFERENCE data (what the model is trained on)
#Normal transaction amounts $50, mostly daytime
np.random.seed(42)
reference_data = pd.DataFrame({
    "transaction_amount": np.random.normal(loc=50, scale=20, size=1000),
    "hour_of_day": np.random.randint(8, 22, size=1000), #daytime hours - 8am to 10pm
    "is_international": np.random.choice([0, 1], size=1000, p=[0.9, 0.1]), #mostly domestic
    "target_fraud": np.random.choice([0, 1], size=1000, p=[0.98, 0.02]) #very few fraud cases
})

#generate CURRENT data(production data - 6 months later)
#DRIFT introduced: Hackers are doing $2 transactions at 3AM
current_data = pd.DataFrame({
    #mean dropped to $30, because of $2 micro-transactions
    "transaction_amount": np.random.normal(loc=30, scale=25, size=1000),
    #hackers operating at midnight from midnight to 5AM
    "hour_of_day": np.random.randint(0, 24, size=1000),
    #more internatinoal fraud attempts
    "is_international": np.random.choice([0, 1], size=1000, p=[0.7, 0.3]),
    #fraud rate increased to 8%
    "target_fraud": np.random.choice([0, 1], size=1000, p=[0.92, 0.08])
})

print("Datasets generated succesfully!")

from evidently.report import Report
from evidently.metric_preset import DataDriftPreset, DataQualityPreset, TargetDriftPreset

#initialize the Evidently Report
#We are asking for Data Drift, Data Quality and Target(label) Drift metrics
fraud_report = Report(metrics=[
    DataDriftPreset(),
    DataQualityPreset(),
    TargetDriftPreset()
])

#Run the comparison
print("Analyzing drift... this may take a few seconds.")
fraud_report.run(reference_data=reference_data, current_data=current_data, column_mapping={
    "target": "target_fraud"
})

#save the interactive report to an HTML file
fraud_report.save_html("fraud_drift_report.html")
print("Drift analysis complete! Report saved as 'fraud_drift_report.html'.")