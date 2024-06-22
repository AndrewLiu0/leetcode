
class Solution:
    def isHappy(self, n: int) -> bool:
        def squareOfDigits(num: int):
            sum = 0
            curr = num
            while(curr != 0):
                sum += (curr % 10) ** 2
                curr = (curr - curr %10)/10
            return sum
        
        input = 0
        hashset = set()
        hashset.add(input)

        while(n !=1):
            n = squareOfDigits(n)
            if(n in hashset):
                return 0
            hashset.add(n)
        return 1
