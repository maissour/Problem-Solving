'''
Optimal stock market strategy

When evaluating stock market trading strategies, it is useful to determine the maximum possible 
profit that can be made by trading a certain stock. Write an algorithm that, given the
daily price of a stock, computes the maximum profit that can be made by buying and selling
that stock. Assume that you are allowed to own no more than 1 share at any time, and that
you have an unlimited budget.
Example 1: The stock price over several days is [2, 5, 1]. The best strategy is to buy a share
on the first day for price 2, then sell it on the second day for price 5, obtaining a profit of 3.
Example 2: The stock price over several days is [2, 5, 1, 3]. The best strategy is to buy a
share on the first day for price 2, then sell it on the second day for price 5, obtaining a profit
of 3; then buy it again on the third day for price 1, and sell it on the fourth day for price 3,
obtaining an overall profit of 5.
'''
from functools import lru_cache
# Solution 1: dynamic programming, top-down, 𝑂(𝑛) time
def max_profit(daily_price):
    @lru_cache(maxsize=None)
    def get_best_profit(day, have_stock):
        """
        Returns the best profit that can be obtained by the end of the day.
        At the end of the day:
        * if have_stock is True, the trader must own the stock;
        * if have_stock is False, the trader must not own the stock.
        """
        if day < 0:
            if not have_stock:
            # Initial state: no stock and no profit.
                return 0
            else:
            # We are not allowed to have initial stock.
            # Add a very large penalty to eliminate this option.
                return -float('inf')
        price = daily_price[day]
        if have_stock:
        # We can reach this state by buying or holding.
            strategy_buy = get_best_profit(day-1, False)-price
            strategy_hold = get_best_profit(day-1, True)
            return max(strategy_buy, strategy_hold)
        else:
        # We can reach this state by selling or avoiding.
            strategy_sell = get_best_profit(day-1, True) + price
            strategy_avoid = get_best_profit(day-1, False)
            return max(strategy_sell, strategy_avoid)
    # Final state: end of last day, no shares owned.
    last_day = len(daily_price)-1
    no_stock = False
    return get_best_profit(last_day, no_stock)

stock_prices = [2, 5, 1, 3]
result = max_profit(stock_prices)
print(f"Example : Max Profit = {result}")

print("#"*20)
# Solution 2: dynamic programming, bottom-up, 𝑂(𝑛) time
def max_profit(daily_price):
    # Initial state: start from a reference cash amount.
    # It can be any value.
    # We use 0 and allow our cash to go below 0 if we need to buy a share.
    cash_not_owning_share = 0
    # High penalty for owning a stock initially:
    # ensures this option is never chosen.
    cash_owning_share =-float('inf')
    for price in daily_price:
        # Transitions to the current day, owning the stock:
        strategy_buy = cash_not_owning_share-price
        strategy_hold = cash_owning_share
        # Transitions to the current day, not owning the stock:
        strategy_sell = cash_owning_share + price
        strategy_avoid = cash_not_owning_share
        # Compute the new states.
        cash_owning_share = max(strategy_buy, strategy_hold)
        cash_not_owning_share = max(strategy_sell, strategy_avoid)
    # The profit is the final cash amount, since we start from
    # a reference of 0.
    return cash_not_owning_share