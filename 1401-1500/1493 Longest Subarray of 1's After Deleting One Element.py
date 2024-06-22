from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        start = 0
        zeroCount = 0
        for i in range(len(nums)):
            if(nums[i] == 0):
                