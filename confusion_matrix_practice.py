from sklearn.metrics import confusion_matrix, classification_report, roc_curve, auc
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_breast_cancer
import matplotlib.pyplot as plt

data = load_breast_cancer()
x = data.data
y = data.target

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

cm = confusion_matrix(y_test, y_pred)
print("Confusion matrix: \n", cm)
print("Classification report:\n", classification_report(y_test, y_pred))

#ROC Curve + AUC Score
y_prob = model.predict_proba(x_test)[:, 1]
fpr, tpr, thresholds = roc_curve(y_test, y_prob)
roc_auc = auc(tpr, fpr)

plt.plot(fpr, tpr)
plt.plot([0, 1], [0,1], color='navy', lw=2, linestyle='--')
plt.xlabel('False Positive Rate')
plt.ylabel('False Negative Rate')
plt.title(f"ROC Curve (AUC = {roc_auc:.3f})")
plt.show()

#dvc run -n train_model -d data/covid19.csv -o model.joblib python wine_train_mlflow.py