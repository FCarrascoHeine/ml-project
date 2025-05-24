# Simple ML Pipeline

**Status:** Under Construction 🚧

This repository is an evolving Python project focused on building a simple, interactive machine learning pipeline. Currently, it allows the user to:

- Choose between two datasets: **Iris** and **Wine**.
- Choose between two classification algorithms: **Logistic Regression** and **Decision Tree**.
- Train the chosen model on the selected dataset and evaluate its accuracy.

## Current Features

- Users can choose among several machine learning algorithms.
- Users can select from a few predefined datasets.
- Basic structure set up for future enhancements.
- **Basic unit and integration tests included**, with tests running automatically on GitHub Actions on pushes and pull requests.
- Dockerfile included, allowing for seamless creation of docker images.

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
2. Run `python -m src.main`.
3. Follow the prompts to select the dataset and model.

## Docker: Build and test images

To build and test a Docker image for this project locally, ensure you have [Docker installed and running](https://docs.docker.com/get-docker/).

1. **Build the image** (assuming the project directory contains the Dockerfile):
```
docker build -t ml-project .
```

2. **Run the container** to test the app inside Docker:
```
docker run -it --rm ml-project
```
This command runs the CLI app interactively inside the container, similar to running `python -m src.main` locally.

This workflow allows you to verify the Dockerized app behaves as expected before pushing the image to a container registry or setting up automated deployment.

## Testing

- Run tests locally with `pytest`
- Tests are automatically run on GitHub Actions for every push and pull request.

## Next Steps

- Adding support for user-provided data.
- Implementing training parameter configuration.
- Setting up Continuous Deployment (CD) to automate deployment.

Feel free to explore and contribute!
