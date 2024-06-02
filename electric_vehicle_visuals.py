import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load the dataset using Pandas
electric_vehicle = pd.read_csv('electric_vehicle.csv')  # Ensure this path is correct relative to your script

# Set the theme
sns.set_theme(style="whitegrid")

# Create a count plot
plt.figure(figsize=(12, 8))  # Optional: Adjust the figure size for better visibility
sns.countplot(x='County', hue='Make', data=electric_vehicle)
plt.title('County Vs Make')
plt.xticks(rotation=90)  # Optional: Rotate x-axis labels if they are too long
plt.show()
