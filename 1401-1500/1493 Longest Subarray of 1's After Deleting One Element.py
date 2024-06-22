from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        i, zeroCount, maxLength = 0, 0, 0
        for j in range(len(nums)):
            if(nums[j] == 0 and zeroCount == 1):
                i = nums.index(0, i) + 1
            elif(nums[j] == 0 and zeroCount == 0):
                zeroCount +=1
            maxLength = max(maxLength, j - i)
        return maxLength