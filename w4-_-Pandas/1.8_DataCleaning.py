import pandas as pd

df = pd.read_csv('1.0_train.csv')

# Check for missing values
print("\nMissing Values Count:")
print(df.isnull().sum())

print("\n----------------------------------------------------------------")

# Fill missing Age values with the mean
df['Age'].fillna(df['Age'].mean(), inplace=True)

# Drop the Cabin column (too many missing values)
df.drop(columns=['Cabin'], inplace=True)

# Fill missing Embarked values with the most frequent value
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

# Display results
print("\nCleaned Data:")
print(df.isnull().sum())
print("\n----------------------------------------------------------------\n")
print(df.head())