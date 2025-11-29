from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report, roc_curve, auc
import numpy as np
import matplotlib.pyplot as plt

#load the california housing dataset
housing = fetch_california_housing(as_frame=True)
df = housing.frame.copy() 

# Define a threshold for "high value" — you can choose e.g. the 75th percentile
threshold = np.percentile(df["MedHouseVal"], 75)
df["high_value"] = (df["MedHouseVal"] > threshold).astype(int)

# Prepare features and new target
X = df[housing.feature_names]
y = df["high_value"]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build and fit classifier
model = LogisticRegression(max_iter=10000)
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:, 1]

# Evaluate
cm = confusion_matrix(y_test, y_pred)
print("Confusion matrix:\n", cm)
print("Classification report:\n", classification_report(y_test, y_pred))

#ROC curve and AUC
fpr, tpr, thresholds = roc_curve(y_test, y_prob)
roc_auc = auc(fpr, tpr)


plt.plot(fpr, tpr, label=f"AUC = {roc_auc:.3f}")
plt.plot([0,1], [0,1], linestyle="--", color="grey")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC — High-value vs Low-value house (California Housing)")
plt.legend()
plt.show()