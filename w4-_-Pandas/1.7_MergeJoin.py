import pandas as pd

df = pd.read_csv('1.0_train.csv')

# Create a sample additional dataset
extra_data = pd.DataFrame({
    'PassengerId': [1, 2, 3, 4, 5],
    'ExtraInfo': ['A', 'B', 'C', 'D', 'E']
})

# Merge
merged_df = pd.merge(df, extra_data, on='PassengerId', how='left')

# Join the datasets (index-based)
df.set_index('PassengerId', inplace=True)
extra_data.set_index('PassengerId', inplace=True)
joined_df = df.join(extra_data, how='left')

print("\nMerge Result:\n")
print(merged_df.head())
print("\n----------------------------------------------------------------")
print("\n\nJoin Result:\n")
print(joined_df.head())