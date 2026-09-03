df = pd.read_csv('MARUTI.NS.csv')
user_y_choice = input("What you want to predict?\n1. Open\n2. High\n3. Low\n4. Close\n5. RSI(Buy/Sell)\nInput: ")

# Map user's choice to actual column names
column_mapping = {
    '1': 'Open',
    '2': 'High',
    '3': 'Low',
    '4': 'Close',
    '5': 'RSI(Buy/Sell)',
    'Open': 'Open',
    'High': 'High',
    'Low': 'Low',
    'Close': 'Close',
    'RSI(Buy/Sell)': 'RSI(Buy/Sell)'
}

user_y = column_mapping.get(user_y_choice, None)

if user_y is None:
    raise ValueError(f"Invalid input for prediction column: {user_y_choice}. Please enter a number between 1 and 5, or the column name directly.")

user_interval = int(input("Number of interval in which you want data to predict: "))
y = df.loc[user_interval:,user_y]
y.index=np.arange(0, len(y))
x = df.drop(['Date', user_y], axis=1).iloc[:-user_interval, :]
# x = x.iloc[:-1, :]
#y = df[['High', 'Low', 'RSI']]
train_accuracy = []
test_accuracy = []
train_rsme = []
test_rsme = []
kfolds = []
kfold_accuracy = []