# Python3 Program to find best buying and selling days for a stock whose prices have been
# price = [100, 180, 260, 310, 40, 535, 695] for last 7 days (n days)

# This function finds the buy sell schedule for maximum profit
def stockBuySell(price, n):     # n is no of days for which prices are provided
    # Prices must be given for at least two days
    if (n == 1):
        return print("Error! Prices for at least 2 days must be provided")

    i = 0
    # profit = 0
    while (i < (n - 1)):

        # Find minimum value
        # Note that the limit is (n-2) as we are comparing present element to the next element
        while ((i < (n - 1)) and (price[i + 1] <= price[i])):
            i = i + 1

        # If we reached the end, break as no further solution possible
        if (i == n - 1):
            break

        # Store the minimum value index
        buy = i
        i = i + 1

        # Find Maximum value
        # Note that the limit is (n-1) as we are comparing to previous element
        while ((i < n) and (price[i] >= price[i - 1])):
            i += 1

        # Store the maximum value index
        sell = i - 1

        print("Buy on day: ", buy+1, "\n", "Sell on day: ", sell+1)
        profit = price[sell] - price[buy]
        print("Profit:", profit)


# Driver code

# Stock prices on consecutive days
# price = [100, 180, 260, 310, 40, 535, 695]
# price = [100]
price = [200, 180, 260, 310, 40, 535, 695]
n = len(price)

# Function call
x = stockBuySell(price, n)
# print(x)