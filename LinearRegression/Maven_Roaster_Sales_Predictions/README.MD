# Linear Regression Models

This notebook implements linear regression models to predict total sales using features such as transaction quantity, unit price, product category, transaction day, and store location.

## Dataset

The dataset used in this notebook contains information about coffee shop sales revenue, including transaction quantity, unit price, product category, transaction day, store location, and total sales.

## Preprocessing the Data

- Selected relevant features for modeling.
- Converted categorical features (product category and store location) to numeric features by mapping them to their corresponding mean total sales.
- Scaled the features using RobustScaler to standardize their ranges.
- You can access data Analysis - EDA of this dataset inside [Data-Analysis](https://github.com/jigsaw1313/Data-Analysis/tree/master) repository or this [link](https://github.com/jigsaw1313/Data-Analysis/tree/master/Maven%20Roasters)

## 1. Linear Regression Model

- Implemented a linear regression model using the scikit-learn library.
- Split the dataset into training and testing sets.
- Trained the linear regression model on the training data.
- Evaluated the model's performance using mean squared error (MSE) and R-squared metrics.

### Results:
- Mean Squared Error: 0.07399622114798542
- R-squared: 0.9271586107849344

## 2. Gradient Descent Linear Regression

- Implemented a gradient descent linear regression model from scratch.
- Used the gradient descent algorithm to optimize the model parameters.
- Evaluated the model's performance using mean squared error (MSE) and R-squared metrics.

### Results:
- Mean Squared Error (Gradient Descent): 0.06263058211964594
- R-squared (Gradient Descent): 0.938346870445999

## 3. Linear Regression Model with SGDRegressor

- Implemented a linear regression model using SGDRegressor from scikit-learn.
- Utilized a pipeline with feature scaling (StandardScaler) and the SGDRegressor model.
- Evaluated the model's performance using mean squared error (MSE) and R-squared metrics.

### Results:
- Mean Squared Error (SGDRegressor): 0.05804683887766444
- R-squared (SGDRegressor): 0.9428590768853435

Overall, the linear regression models provide insights into the relationship between various features and total sales in coffee shop transactions.
