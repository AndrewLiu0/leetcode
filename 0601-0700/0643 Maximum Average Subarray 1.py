from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum = 0
        for i in range (k):
            sum += nums[i]
        maxSum = sum
        for i in range(len(nums) - k):
            sum += nums[k+i] - nums[i]
            maxSum = max(maxSum, sum)
        return maxSum/k

sol = Solution()
print(sol.findMaxAverage([1,12,-5,-6,50,3], 4))