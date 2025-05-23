from utils import choose_option
from ml_pipeline import run_ml_pipeline

def main():
    dataset_names = ["Iris", "Wine"]
    model_names = ["Logistic Regression", "Decision Tree"]

    dataset_idx = choose_option(dataset_names, "Choose a dataset:")
    model_idx = choose_option(model_names, "Choose a model:")

    accuracy = run_ml_pipeline(dataset_names[dataset_idx], model_names[model_idx])

    print(f"\nModel: {model_names[model_idx]}")
    print(f"Dataset: {dataset_names[dataset_idx]}")
    print(f"Accuracy: {accuracy:.2f}")

if __name__ == "__main__":
    main()
