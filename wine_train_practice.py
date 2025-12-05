import joblib
from sklearn.datasets import load_wine
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

data = load_wine()
X = data.data
y = data.target

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_stae=42)

model = DecisionTreeClassifier()
model.fit(x_train, y_train)

joblib.dump(model, 'wine_model.pkl')
print("Model saved as\n'wine_model.pkl")