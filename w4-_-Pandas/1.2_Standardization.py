"""
This file standardizes numerical data (mean = 0, standard deviation = 1).
"""

import pandas as pd
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('1.0_train.csv')

print(df.head())

print("--------------------------------\n")

# Select numerical columns
numeric_cols = ['Age', 'Fare']
df_numeric = df[numeric_cols].dropna()  # Drop missing values


scaler = StandardScaler()
df_standardized = scaler.fit_transform(df_numeric)


df_standardized = pd.DataFrame(df_standardized, columns=numeric_cols)

print("Standardized Data:")
print(df_standardized.head())


print("\nMean:\n", df_standardized.mean())
print("\nStandard Deviation:\n", df_standardized.std())