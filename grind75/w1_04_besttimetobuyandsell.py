def maxProfit(self, prices: List[int]) -> int:
    max_profit, cur_low = 0, sys.maxint
    for price in prices:
        if price - cur_low > max_profit:
            max_profit = price - cur_low
        if price < cur_low:
            price = cur_low
    return max_profit
