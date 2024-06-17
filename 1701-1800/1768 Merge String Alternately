
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        rtn = ""
        for i in range (min(len(word1), len(word2))):
            rtn = f'{rtn}{word1[i]}{word2[i]}'

        if(len(word1) > len(word2)): 
            rtn += word1[i+1:] 
        else:
            rtn += word2[i+1:]

        return rtn

    

'''
Three Cases;
- w1 & w2 same length
- w1 > w2 
- w2 > s1

'''
