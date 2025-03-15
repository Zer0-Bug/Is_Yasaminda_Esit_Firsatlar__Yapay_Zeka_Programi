import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, MinMaxScaler

df = pd.read_csv('2.0_train.csv')

print("Original Data (First 5 rows):")
print(df[['Id', 'LotFrontage', 'GarageCars', 'LotArea', 'GrLivArea', 'SalePrice']].head())

print("\n----------------------------------------------------------------")

# Data Cleaning
print("Before Cleaning (Missing Values):")
print(df[['LotFrontage', 'GarageCars', 'Alley', 'PoolQC']].isnull().sum())

df['LotFrontage'].fillna(df['LotFrontage'].mean(), inplace=True)
df.drop(columns=['Alley', 'PoolQC', 'Fence', 'MiscFeature'], inplace=True)
df['GarageCars'].fillna(df['GarageCars'].mode()[0], inplace=True)

print("\nAfter Cleaning (Missing Values):")
print(df[['LotFrontage', 'GarageCars']].isnull().sum())
print("\nCleaned Data (First 5 rows):")
print(df[['Id', 'LotFrontage', 'GarageCars', 'LotArea', 'GrLivArea', 'SalePrice']].head())

print("\n----------------------------------------------------------------")


# Standardization
print("Before Standardization (First 5 rows):")
print(df[['LotArea', 'GrLivArea', 'SalePrice']].head())

scaler_std = StandardScaler()
df[['LotArea', 'GrLivArea', 'SalePrice']] = scaler_std.fit_transform(
    df[['LotArea', 'GrLivArea', 'SalePrice']].fillna(0)
)

print("\nAfter Standardization (First 5 rows):")
print(df[['LotArea', 'GrLivArea', 'SalePrice']].head())

print("\n----------------------------------------------------------------")


# Normalization
print("Before Normalization (Original Values, First 5 rows):")
print(df[['LotArea', 'GrLivArea', 'SalePrice']].head())

scaler_norm = MinMaxScaler()
df_normalized = pd.DataFrame(
    scaler_norm.fit_transform(df[['LotArea', 'GrLivArea', 'SalePrice']].fillna(0)),
    columns=['LotArea', 'GrLivArea', 'SalePrice']
)

print("\nAfter Normalization (First 5 rows):")
print(df_normalized.head())

print("\n----------------------------------------------------------------")


# Visualization
plt.figure(figsize=(10, 6))
plt.hist(df['SalePrice'], bins=20, color='salmon', edgecolor='black')
plt.title('Standardized Sale Price Distribution')
plt.xlabel('Sale Price (Standardized)')
plt.ylabel('Frequency')
plt.show()

print("\n----------------------------------------------------------------")


# GroupBy
print("Before Grouping (Sample Data):")
print(df[['Neighborhood', 'SalePrice']].head())

grouped = df.groupby('Neighborhood')['SalePrice'].mean()
print("\nAfter Grouping (Average Sale Price by Neighborhood):")
print(grouped.head())

print("\n----------------------------------------------------------------")


# Filtering
print("Before Filtering (Sample Data):")
print(df[['Id', 'OverallQual', 'GrLivArea', 'SalePrice']].head())

filtered = df.query("OverallQual > 7 and GrLivArea > 1500")
print("\nAfter Filtering (High-Quality and Large Houses):")
print(filtered[['Id', 'OverallQual', 'GrLivArea', 'SalePrice']].head())

print("\n----------------------------------------------------------------")


# Merge
print("Before Merging (Sample Data):")
print(df[['Id', 'SalePrice']].head())

extra_data = pd.DataFrame({
    'Id': [1, 2, 3, 4, 5],
    'OwnerName': ['John', 'Alice', 'Bob', 'Emma', 'Mike']
})

merged_df = pd.merge(df, extra_data, on='Id', how='left')


print("\nAfter Merging (With Extra Data):")
print(merged_df[['Id', 'SalePrice', 'OwnerName']].head())