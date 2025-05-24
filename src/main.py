from sklearn.datasets import load_iris, load_wine
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier

from src.chooser import OptionChooser
from src.trainer import MLTrainer

def main() -> None:
    """
    Executes a simple, interactive machine learning pipeline.

    Steps:
    - Choose between two datasets: Iris and Wine.
    - Choose between two classification algorithms: Logistic Regression and Decision Tree.
    - Train the chosen model on the selected dataset and evaluate its accuracy.
    """
    datasets = {
        "Iris": load_iris,
        "Wine": load_wine
    }
    models = {
        "Logistic Regression": LogisticRegression(max_iter=200),
        "Decision Tree": DecisionTreeClassifier()
    }

    dataset_chooser = OptionChooser(list(datasets.keys()), "Choose a dataset:")
    model_chooser = OptionChooser(list(models.keys()), "Choose a model:")

    dataset_name = list(datasets.keys())[dataset_chooser.get_choice()]
    model_name = list(models.keys())[model_chooser.get_choice()]

    data = datasets[dataset_name]()
    model = models[model_name]

    trainer = MLTrainer(model, data) # type: ignore
    accuracy = trainer.train_and_evaluate()

    print(f"\nModel: {model_name}")
    print(f"Dataset: {dataset_name}")
    print(f"Accuracy: {accuracy:.2f}")

if __name__ == "__main__":
    main()
