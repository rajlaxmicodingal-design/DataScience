# Import libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
 

# Load dataset
HouseDF = pd.read_csv('D:\Codingal\Data Science\M12\Lesson 5 – Visualization with Data Science V\Housing.csv')

# Display first few rows
HouseDF.head()

# Display dataset information
HouseDF.info()

# Display column names
HouseDF.columns

# Create pairplot
sns.pairplot(HouseDF)

# Create heatmap of correlations
sns.heatmap(HouseDF.corr(), annot=True)