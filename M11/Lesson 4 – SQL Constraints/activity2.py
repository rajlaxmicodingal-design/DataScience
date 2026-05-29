#Import 
"""
from google.colab import files
uploaded = files.upload()
"""

# Connect with sqlite database
# Import necessary libraries
import pandas as pd
import numpy as np

import sqlite3

database = 'D:/Codingal/Data Science/M11/database.sqlite'

conn = sqlite3.connect(database)
print('Opened data successfully')

# Display all the tables of the database
df = pd.read_sql("""SELECT * 
                    FROM sqlite_master
                    WHERE type='table';""", conn)
print(df)

# Display the first five rows of the Player_Match table
player_match = pd.read_sql("""SELECT *
                        FROM Player_Match""", conn)

print(player_match.head())

# Check the presence of null values in the Player_Match table
null_player_match = pd.read_sql("""SELECT *
                        FROM Player_Match
                        WHERE Team_Id IS NULL""", conn)

print(null_player_match)

# Display the first five rows of the Match table
toss_dec = pd.read_sql("""SELECT *
                        FROM Match""", conn)

print(toss_dec.head())

# Check the presence of null values in the Match table
null_match = pd.read_sql("""SELECT *
                        FROM Match
                        WHERE MATCH_Winner IS NULL""", conn)

print(null_match)

