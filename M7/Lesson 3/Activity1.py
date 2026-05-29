# Program to find the max profit you can get from buying and selling stocks. You are given an array with stocks price for seven days, and you can buy and sell any day. 
 
def calculateProfits(arr,arr_size):
 
    profit = 0
    for i in range(1, arr_size):
 
        # If the current element is greater than last element then we will but the previous day and sell it the current day.
        if arr[i] > arr[i-1]:
 
            # calculate profit
            profit += arr[i] - arr[i-1]
 
    return profit
 
# Prices for 7 days
prices = [635,864,247,325,257,745,245]
 
profit = calculateProfits(prices, len(prices))
print("Max profit : ",profit)
