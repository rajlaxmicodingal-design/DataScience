import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

Titanic = pd.read_csv(r"D:\Codingal\Data Science\M16\Lesson 2 – Understanding more about Data\titanic.csv", sep='\t') # Fixed: added sep='\t' to correctly parse the CSV.
print(Titanic.head())

print(Titanic.shape)

print(Titanic.isnull().sum())

sns.heatmap(Titanic.isnull(), cmap="spring")

#Since the highest null values are found in "Cabin" coloumn so dropping it respectively..

#Printing the original Dataset again

print(Titanic.head())

#Dropping the Cabin coloumn

Titanic.drop("Cabin", axis=1, inplace=True) # Fixed: Changed 'deck' to 'Cabin' as 'Cabin' is the correct column name with deck-related info.

#Printing the Dataset after dropping the coloumn

print(Titanic.head())

Titanic.dropna(inplace=True)

sns.heatmap(Titanic.isnull(), cbar=False)

#As you can see no null values found

#Now all the null values have been removed "CHECK"

print(Titanic.isnull().sum())

#Simplifying the data more by converting the string data types to integer.

print(pd.get_dummies(Titanic["Sex"]).head()) # Corrected column name from 'sex' to 'Sex'

sex = pd.get_dummies(Titanic["Sex"], drop_first=True) # Corrected column name from 'sex' to 'Sex'

print(sex.head(4))

#If we observe embark_town there are only two data types present which can be split in the form of integers

print(pd.get_dummies(Titanic["Embarked"]).head(4)) # Corrected column name from 'embarked' to 'Embarked'

arked = pd.get_dummies(Titanic["Embarked"], drop_first=True) # Corrected column name from 'embarked' to 'Embarked'

#Similarly for pclass

pclass = pd.get_dummies(Titanic["Pclass"], drop_first=True) # Corrected column name from 'pclass' to 'Pclass'

print(pclass.head(4))

Titanic = pd.concat([Titanic, sex, pclass], axis=1)

#Printing the Updated Dataset
print(Titanic.head())