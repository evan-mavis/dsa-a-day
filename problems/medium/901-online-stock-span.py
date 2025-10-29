from collections import deque

class StockSpanner:
    def __init__(self):
        self.stack = []  # Stack of (price, span) tuples

    def next(self, price: int) -> int:
        span = 1  # At least today counts
        
        # Pop all prices <= current price and accumulate their spans
        while self.stack and self.stack[-1][0] <= price:
            prev_price, prev_span = self.stack.pop()
            span += prev_span  # Add the span of days that were <= this price
        
        # Push current price with its span
        self.stack.append((price, span))
        
        return span
        