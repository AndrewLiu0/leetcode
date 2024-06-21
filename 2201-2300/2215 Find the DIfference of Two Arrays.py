
from typing import List

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        num1Set = set(nums1)
        num2Set = set(nums2)

        num1Final = num1Set.copy()

        for element in num1Set:
            if(element in num2Set):
                num1Final.remove(element)
                num2Set.remove(element)
        arr = [list(num1Final), list(num2Set)]
        return arr

sol = Solution()
print(sol.findDifference([1,2,3],[2,4,6]))