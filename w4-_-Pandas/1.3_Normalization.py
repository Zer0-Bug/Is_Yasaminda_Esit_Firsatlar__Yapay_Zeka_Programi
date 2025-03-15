"""
This file normalizes data to a 0-1 range (Min-Max Normalization).
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler


df = pd.read_csv('1.0_train.csv')

print(df.head())

print("--------------------------------\n")

numeric_cols = ['Age', 'Fare']
df_numeric = df[numeric_cols].dropna()

scaler = MinMaxScaler()
df_normalized = scaler.fit_transform(df_numeric)

df_normalized = pd.DataFrame(df_normalized, columns=numeric_cols)

print("Normalized Data:")
print(df_normalized.head())

# Check min and max values
print("\nMinimum:", df_normalized.min())
print("Maximum:", df_normalized.max())