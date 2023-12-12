class Solution:
    def totalMoney(self, n: int) -> int:
        def calaculate(a: int, b: int) -> int:
            return (a + b) * (b - a + 1) // 2

        weeks = n // 7
        initial = calaculate(1, 7)
        last = calaculate(1 + weeks - 1, 7 + weeks - 1)
        rest = calaculate(1 + weeks, n % 7 + weeks)
        return (initial + last) * weeks // 2 + rest