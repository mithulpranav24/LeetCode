"""import numpy as np
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if (np.log(n)/np.log(2)) % 1 == 0:
            return True
        else:
            return False

print(Solution().isPowerOfTwo(536870912))



print(np.log(536870912)/np.log(2))
"""
"""
import numpy as np

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        val = np.log(n) / np.log(2)
        return np.isclose(val, round(val))

print(Solution().isPowerOfTwo(16383))"""

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        return (n & (n - 1)) == 0
