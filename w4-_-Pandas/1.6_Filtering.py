import pandas as pd

df = pd.read_csv('1.0_train.csv')

# Select
selected_cols = df[['PassengerId', 'Survived', 'Pclass', 'Age']]

# Where: Filter passengers older than 30
where_filtered = df[df['Age'] > 30]

# Query: Filter female passengers in 1st class
query_filtered = df.query("Sex == 'female' and Pclass == 1")

print("\n\nSelected Columns:\n")
print(selected_cols.head())
print("\n----------------------------------------------------------------")
print("\n\nPassengers Older Than 30:\n")
print(where_filtered.head())
print("\n----------------------------------------------------------------")
print("\n\nFemale and 1st Class Passengers:\n")
print(query_filtered.head())