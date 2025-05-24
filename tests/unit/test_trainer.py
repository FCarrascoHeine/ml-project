from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from src.trainer import MLTrainer


def test_train_and_evaluate() -> None:
    # Check if training a model results in a valid accuracy value 
    data = load_iris()
    model = LogisticRegression(max_iter=200)
    trainer = MLTrainer(model, data)
    accuracy = trainer.train_and_evaluate()
    assert isinstance(accuracy, float)
    assert 0.0 <= accuracy <= 1.0
