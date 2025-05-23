# Simple ML Pipeline

Status: Under Construction 🚧

This repository is an evolving Python project focused on building a simple, interactive machine learning pipeline. Currently, it allows the user to:

- Choose between two datasets: **Iris** and **Wine**.
- Choose between two classification algorithms: **Logistic Regression** and **Decision Tree**.
- Train the chosen model on the selected dataset and evaluate its accuracy.

## Current Features

- Users can choose among several machine learning algorithms.
- Users can select from a few predefined datasets.
- Basic structure set up for future enhancements.

## What the script does now

- **Datasets**:
  - **Iris**: A classic dataset containing measurements of iris flowers from three different species. The task is to predict the species based on flower features.
  - **Wine**: Contains chemical analysis results of wines grown in the same region in Italy but derived from three different cultivars. The task is to predict the wine cultivar based on the chemical properties.

- **Models**:
  - **Logistic Regression**: A linear model used for classification.
  - **Decision Tree**: A tree-based model that splits the data according to feature values.

- The script splits the data into training and test sets using the default 75% training, 25% test split (from scikit-learn’s `train_test_split`).
- It trains the chosen model on the training set, makes predictions on the test set, and then outputs the accuracy score.

## How to run

1. Make sure you have the required packages installed (see `requirements.txt`).
2. Run `python main.py`.
3. Follow the prompts to select the dataset and model.

## Next Steps

- Adding support for user-provided data.
- Implementing training parameter configuration.
- Writing tests and setting up CI/CD.
- Automating deployment.
