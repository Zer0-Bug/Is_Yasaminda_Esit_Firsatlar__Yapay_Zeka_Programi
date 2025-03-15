import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('1.0_train.csv')

# Histogram of age distribution
plt.figure(figsize=(10, 6))
plt.hist(df['Age'].dropna(), bins=20, color='skyblue', edgecolor='black')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# Boxplot of fare
plt.figure(figsize=(10, 6))
plt.boxplot(df['Fare'].dropna())
plt.title('Fare Distribution')
plt.ylabel('Fare')
plt.show()