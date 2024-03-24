import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.float_format', lambda x: '%.0f' % x)

# Load the dataset
df = pd.read_csv('world_pop.csv')

population_2020 = df[['country','year_2020']]
# print(population_2020)

top_10_2020 = population_2020.sort_values(by='year_2020', ascending=False).head(10)

plt.figure(figsize=(10, 7))
plt.barh(top_10_2020['country'], top_10_2020['year_2020'], color='skyblue')
plt.xlabel('Population (in billions)', fontsize=14)
plt.ylabel('Country', fontsize=14)
plt.title('Top 10 Most Populous Countries in 2020', fontsize=18)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.gca().invert_yaxis()
plt.grid(axis='x')
plt.tight_layout()
plt.show()