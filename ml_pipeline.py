from sklearn.datasets import load_iris, load_wine
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

def run_ml_pipeline(dataset_name, model_name):
    datasets = {
        "Iris": load_iris,
        "Wine": load_wine
    }
    models = {
        "Logistic Regression": LogisticRegression(max_iter=200),
        "Decision Tree": DecisionTreeClassifier()
    }

    data = datasets[dataset_name]()
    X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, random_state=42)

    model = models[model_name]
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    accuracy = accuracy_score(y_test, preds)

    return accuracy
