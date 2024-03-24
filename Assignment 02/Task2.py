import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.float_format', lambda x: '%.0f' % x)

# Load the dataset
df = pd.read_csv('world_pop.csv')

population_2020 = df[['country','year_2015']]
# print(population_2020)

top_10_2020 = population_2020.sort_values(by='year_2015', ascending=True).head(10)

plt.figure(figsize=(10, 7))
plt.barh(top_10_2020['country'], top_10_2020['year_2015'], color='skyblue')
plt.xlabel('Population (in billions)', fontsize=14)
plt.ylabel('Country', fontsize=14)
plt.title('Top 10 Least Populous Countries in 2015', fontsize=18)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.gca().invert_yaxis()
plt.grid(axis='x')
plt.tight_layout()
plt.show()
print()

countries = ['Pakistan', 'India', 'United States', 'United Kingdom']
years = ['year_' + str(year) for year in range(1970, 2011)]  # Generate column names for years 1970 to 2010
population_data = df.loc[df['country'].isin(countries), ['country'] + years]

# Set the 'Country' column as the index
population_data.set_index('country', inplace=True)

# Transpose the DataFrame to have years as index and countries as columns
population_data = population_data.transpose()

# Plot a line chart showing the population change over time for each country
plt.figure(figsize=(12, 8))
for country in population_data.columns:
    plt.plot(population_data.index, population_data[country], label=country)

plt.title('Population Change (1970-2010)', fontsize=18)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Population', fontsize=14)
plt.xticks(rotation=45)
plt.legend(fontsize=12)
plt.grid(True)
plt.tight_layout()
plt.show()

print()


years = [f'year_{year}' for year in range(2010, 2021)]
population_data = df.loc[df['country'] == 'Pakistan', years]

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(years, population_data.values[0], marker='o', linestyle='-')
plt.xlabel('Year', fontsize=14)
plt.ylabel('Population', fontsize=14)
plt.title('Population Growth of Pakistan (2010-2020)', fontsize=18)
plt.grid(True)
plt.tight_layout()
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.show()

