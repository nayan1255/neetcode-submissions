class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        n, m = len(word1), len(word2)
        res = ""
        while i < n and i < m:
            res = res + word1[i]
            res = res + word2[i]
            i+=1
        
        res += word1[i:]
        res += word2[i:]
        
        return res