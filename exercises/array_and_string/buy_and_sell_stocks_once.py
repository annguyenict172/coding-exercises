"""
Buy and Sell Stocks Once: EPI 5.6
"""


def calculate_max_profit(prices):
    if len(prices) <= 1:
        return 0

    lowest_price = prices[0]
    max_profit = 0
    for i in range(1, len(prices)):
        current_price = prices[i]
        max_profit = max(max_profit, current_price - lowest_price)
        lowest_price = min(lowest_price, current_price)

    return max_profit
