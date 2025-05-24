from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

class MLTrainer:
    """Creates objects used to store the chosen data and model."""
    def __init__(self, model, data):
        self.model = model
        self.data = data

    def train_and_evaluate(self):
        # Train and evaluate the model chosen by the user
        X_train, X_test, y_train, y_test = train_test_split(
            self.data.data, self.data.target, random_state=42
        )
        self.model.fit(X_train, y_train)
        preds = self.model.predict(X_test)
        accuracy = accuracy_score(y_test, preds)
        return accuracy
