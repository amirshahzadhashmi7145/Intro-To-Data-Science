import pandas as pd
import matplotlib.pyplot as plt

# Load the diamonds dataset
df = pd.read_csv('diamonds.csv')

# Filter the dataset for diamonds with 'clarity' = 'SI2' and 'color' = 'E'
filtered_df = df[(df['clarity'] == 'SI2') & (df['color'] == 'E')]

# Plot the relationship between 'carat' and 'price' with different colors for each 'cut'
plt.figure(figsize=(10, 6))
for cut, group in filtered_df.groupby('cut'):
    plt.scatter(group['carat'], group['price'], label=cut)

# Add labels and title
plt.xlabel('Carat', fontsize=14)
plt.ylabel('Price', fontsize=14)
plt.title('Relationship between Carat and Price of Diamonds (Clarity: SI2, Color: E)', fontsize=18)

# Add legend
plt.legend(title='Cut', fontsize=12)

# Set grid
plt.grid(True)

# Show plot
plt.tight_layout()
plt.show()
