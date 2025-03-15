import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('1.0_train.csv')

# Group by ticket class and calculate mean survival rate
grouped = df.groupby('Pclass')['Survived'].mean()

print("Survival Rate by Ticket Class:")
print(grouped)

grouped.plot(kind='bar', color='lightgreen', edgecolor='black')
plt.title('Survival Rate by Ticket Class')
plt.xlabel('Ticket Class')
plt.ylabel('Mean Survival Rate')
plt.show()