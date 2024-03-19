# Linear Regression Model for Taxis Dataset

This notebook implements a linear regression model to predict the total fare for taxi trips based on various features such as the number of passengers, distance traveled, fare amount, tip amount, and tolls paid.

## Dataset

The dataset contains information about taxi trips, including the number of passengers, distance traveled, fare amount, tip amount, tolls paid, and total fare. 

## Data Preprocessing

- Checked dataset information and descriptive statistics.
- Removed rows with missing values.
- Detected and removed outliers using the Interquartile Range (IQR) method.
- Scaled the numerical features using both RobustScaler and StandardScaler to standardize their ranges.
- Checked the distributions of features to ensure data normality.
- Calculated the correlation matrix to identify relationships between features.

## Linear Regression Model

- Selected features ('passengers', 'distance', 'fare', 'tip', 'tolls') as independent variables and 'total' as the target variable.
- Split the dataset into training and testing sets.
- Trained a linear regression model using the scikit-learn library.
- Made predictions on the test set.
- Evaluated the model's performance using mean squared error (MSE) and R-squared metrics.
- Displayed the model's intercept and coefficients.

### Results:

- Mean Squared Error : 0.0061139401551850775
- R-squared : 0.9928824103035198
- model intercept : -0.00023670765264818122
- model coef : [ 0.00620096 -0.0167029   0.818179    0.21575411  0.10724279]

Overall, the linear regression model provides insights into the factors affecting the total fare for taxi trips and can be used for predicting fare amounts based on input features.
