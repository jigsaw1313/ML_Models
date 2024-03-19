# -*- coding: utf-8 -*-
"""Taxis_Dataset_Seaborn_LinearRegression_Model.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1J6c4x3nlR3SR-Ked_fJipQhdUb5DvLmB

# Import Dataset and Libraries
"""

import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=sns.load_dataset('taxis')
df.head()

"""# Check Dataset"""

df.info()

df.describe().T

"""# Data Scaling and Handling Missing Value"""

df.dropna(inplace=True)

"""## Detect Outliers"""

for col in ['passengers',	'distance'	,'fare'	,'tip'	,'tolls'	,'total']:

  plt.boxplot(df[col], showmeans=True)
  plt.title(f"{col}")
  plt.show()

# Removie outliers using IQR
def remove_outliers_iqr(df, feature):
    Q1 = np.quantile(df[feature], 0.25)
    Q3 = np.quantile(df[feature], 0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return df[(df[feature] >= lower_bound) & (df[feature] <= upper_bound)]

columns = ['passengers',	'distance'	,'fare'	,'tip'	,'tolls'	,'total']
for col in columns:
  remove_outliers_iqr(df, col)

df.reset_index(inplace=True, drop=True)
df.info()

"""## Check Distributions"""

df.hist(bins=150, color='r')

"""## Data Scaling"""

from sklearn.preprocessing import RobustScaler
scaler = RobustScaler()
for col in df.select_dtypes(['int', 'float']):
  df[col] = scaler.fit_transform(df[[col]])

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
for col in df.select_dtypes(['int', 'float']):
  df[col] = scaler.fit_transform(df[[col]])
df.head()

"""## Data Corralation"""

df.corr(numeric_only=True)

"""# Linear Regression"""

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression

# Choosing Features
X = df[['passengers', 'distance', 'fare', 'tip', 'tolls']]
y = df['total']

# Spliting Train & Test Data
X_train , X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Training The Model
model = LinearRegression()
model.fit(X_train, y_train)

# Prediction
y_pred=model.predict(X_test)

# Mean Squared Error & R2 Score
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
# Show result
print(f"\n\nMean Squared Error : {mse}")
print(f"R-squared : {r2}")
print(f"model intercept : {model.intercept_}")
print(f"model coef : {model.coef_}")



