from sklearn.tree import DecisionTreeClassifier
import joblib
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

data = load_breast_cancer()
x = data.data
y = data.target

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.2, random_state=42)

model = DecisionTreeClassifier()
model.fit(x_train, y_train)

joblib.dump(model, 'breast_cancer_model.pkl')
print("Model successfully saved as\n'breast_cancer_model.pkl'")
