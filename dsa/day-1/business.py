def maxProfit(prices):
    min_price = float('inf')  # Step 1: Track lowest price seen so far
    max_profit = 0            # Step 2: Track best profit so far

    for price in prices:
        if price < min_price:
            min_price = price  # update if we find a lower price
        else:
            profit = price - min_price  # check profit if we sell now
            max_profit = max(max_profit, profit)

    return max_profit
