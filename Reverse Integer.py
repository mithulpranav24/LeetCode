class Solution:
    def reverse(self, n: int) -> int:
        s = -1 if n < 0 else 1
        n = abs(n)
        m = 0
        while n > 0:
            rem = n % 10
            m = 10 * m + rem
            n = n // 10
        if s == -1:
            m = m * -1
        if m >= -2**31 and m <= 2**31 - 1:
            return m
        else:
            return 0