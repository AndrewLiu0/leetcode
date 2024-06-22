from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i = 0
        j = 0
        zeroCount = 0
        maxLength = j - i
        while(j < len(nums)):
            if(nums[j] == 0 and zeroCount < k):
                zeroCount += 1
            elif (nums[j] == 0 and zeroCount >=k):
                while(nums[i] != 0):
                    i += 1
                i += 1
            j+=1
            maxLength = max(maxLength, j-i)
        return maxLength

