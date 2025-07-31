class Solution:
    def isHappy(self, n: int) -> bool:
        return self.rec(n)

    def sumofsquares(self, n: int) -> int:
        s = 0
        while n > 0:
            r = n % 10
            s += r * r
            n = n // 10
        return s

    def rec(self, n: int, seen=None) -> bool:
        if seen is None:
            seen = set()

        if n == 1:
            return True
        if n in seen:   # cycle detected
            return False

        seen.add(n)
        return self.rec(self.sumofsquares(n), seen)
