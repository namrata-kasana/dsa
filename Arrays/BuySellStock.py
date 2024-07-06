def max_profit(prices):
  """
  Finds the maximum profit achievable by buying and selling a stock multiple times.

  Args:
      prices: A list of integers representing stock prices on each day.

  Returns:
      The maximum profit possible.
  """
  profit = 0
  for i in range(1, len(prices)):
    if prices[i] > prices[i-1]:
      profit += prices[i] - prices[i-1]
  return profit

# Example usage
prices = [7, 1, 5, 3, 6, 4]
max_profit_value = max_profit(prices)
print(f"Maximum profit: {max_profit_value}")