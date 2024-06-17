import math

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for i in range (int(math.sqrt(c)) + 1):
            remainder_root = math.sqrt(c - i**2)
            if remainder_root == int(remainder_root):
                return True
        return False
