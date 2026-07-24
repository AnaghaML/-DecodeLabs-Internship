# Iris Classification

A basic machine learning classification project built using Python and Scikit-learn.

## About the Project

This project uses the Iris dataset to train a machine learning model that classifies flowers into three species:

- Setosa
- Versicolor
- Virginica

The classification is based on four measurements:

- Sepal Length
- Sepal Width
- Petal Length
- Petal Width

## Workflow

1. Load the Iris dataset
2. Separate features and target values
3. Split the data into training and testing sets
4. Standardize the feature values
5. Train a K-Nearest Neighbors (KNN) classifier
6. Predict the flower species
7. Evaluate the model accuracy

## Technologies Used

- Python
- Scikit-learn

## Model Used

**K-Nearest Neighbors (KNN)**

The model was trained using 80% of the dataset and tested using the remaining 20%.

## Result

The model achieved an accuracy of:

**100%**

The model was also tested with new flower measurements and successfully predicted the flower species.

## How to Run

Install the required library:

```bash
pip install scikit-learn
