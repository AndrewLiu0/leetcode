from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zeroes = nums.count(0)
        for i in range (zeroes):
            nums.remove(0)
        nums += zeroes*[0]

        