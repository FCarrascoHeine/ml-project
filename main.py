from sklearn.datasets import load_iris, load_wine
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

def choose_option(options, prompt):
    print(prompt)
    for i, option in enumerate(options):
        print(f"{i + 1}. {option}")
    choice = input("Enter the number of your choice: ")
    try:
        choice_idx = int(choice) - 1
        if 0 <= choice_idx < len(options):
            return choice_idx
    except ValueError:
        pass
    print("Invalid choice, please try again.")
    return choose_option(options, prompt)

def main():
    datasets = {
        "Iris": load_iris,
        "Wine": load_wine
    }
    models = {
        "Logistic Regression": LogisticRegression(max_iter=200),
        "Decision Tree": DecisionTreeClassifier()
    }

    dataset_names = list(datasets.keys())
    model_names = list(models.keys())

    dataset_idx = choose_option(dataset_names, "Choose a dataset:")
    model_idx = choose_option(model_names, "Choose a model:")

    data = datasets[dataset_names[dataset_idx]]()
    X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, random_state=42)

    model = models[model_names[model_idx]]
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    accuracy = accuracy_score(y_test, preds)

    print(f"\nModel: {model_names[model_idx]}")
    print(f"Dataset: {dataset_names[dataset_idx]}")
    print(f"Accuracy: {accuracy:.2f}")

if __name__ == "__main__":
    main()
