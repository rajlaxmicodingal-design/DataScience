####**Import Libraries**

# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

"""####**Import Dataset**"""

from google.colab import files
uploaded = files.upload()

# Import dataset
data = pd.read_csv('Titanic Dataset.csv')

data.head(5)

"""#### **Passengers belonging from which gender survived the most**"""

sns.countplot(x='Gender', hue='Survived', data=data)
plt.show()
"""#### **Passengers belonging from which PClass survived the most and the least**"""

sns.countplot(x='Pclass', hue='Survived', data=data)
plt.show()
"""#### **Highest number of passengers belong to which Age**"""

sns.histplot(data['Age'],kde=False,bins=40)
plt.show()
"""#### **Highest number of passengers belong to which Gender**"""

sns.countplot(x='Gender', data=data)
plt.show()
"""#### **Is SibSp correlated/associated with Survived feature**"""

sns.countplot(x='Survived', hue='SibSp', data=data, palette="mako")
plt.show()
"""#### **Is Parch correlated/associated with Survived feature**"""

sns.countplot(x='Survived', hue='Parch', data=data, palette="mako")
plt.show()
"""#### **Is the feature Fare having normal distribution/spread of data**"""

sns.histplot(data['Fare'])
plt.show()

"""#### **Check the age group of majority of people belonging to PClass=1**"""

sns.boxplot(x='Pclass',y='Age',data=data, hue=None)
plt.show()
"""#### **Check the correlation of all the features with target variable ‘Survived’**"""

sns.heatmap(data.corr(numeric_only=True))
plt.show()