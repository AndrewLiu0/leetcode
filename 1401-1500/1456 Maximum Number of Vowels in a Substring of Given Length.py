class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowelSet = set(['a','e','i','o','u'])
        currCount = 0
        maxCount = 0

        for char in s[0:k]:
            if char in vowelSet:
                currCount +=1
        maxCount = currCount

        i = 0
        j = k - 1

        while( j < len(s) - 1):
            if(s[i] in vowelSet):
                currCount -= 1
            i += 1
            j += 1
            if(s[j] in vowelSet):
                currCount += 1
            maxCount = max(maxCount, currCount)

        return maxCount


sol = Solution()
print(sol.maxVowels("abciiidef", 3))