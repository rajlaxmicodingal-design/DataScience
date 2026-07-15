import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from google.colab import files
file = files.upload()

data = pd.read_csv('Pokemon Data.csv')
data.head()

data.info()

data['Type 2'].fillna(value='None',inplace=True)
data.isnull().sum()

data['Type 1'].value_counts().plot.bar()
data['Type 2'].value_counts().plot.bar()
data['Legendary'].value_counts().plot.bar()

data['Type 1'].unique()
data['Type 2'].unique()

from sklearn.preprocessing import LabelEncoder
lb = LabelEncoder()
data['Legendary'] = lb.fit_transform(data['Legendary'])

data.head()

data.drop('Name', axis=1, inplace=True)
# Drop the '#' column as it's an identifier and not a feature for the model
data.drop('#', axis=1, inplace=True)

data = pd.get_dummies(data)

data.shape

from sklearn.model_selection import train_test_split
y = data.pop('Legendary')
X = data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
LogReg = LogisticRegression()
LogReg.fit(X_train,y_train)
ypred1 = LogReg.predict(X_test)
accuracy_score(y_test,ypred1)