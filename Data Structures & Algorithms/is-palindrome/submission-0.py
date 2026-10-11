# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         val = ""
#         for char in s:
#             if char.isalnum():
#                 val += char.lower()
#         return (val == val[::-1])

class Solution:
    def isPalindrome(self, s: str) -> bool:
        val = ""
        for char in s:
            if char.isalnum():
                val += char.lower()
        
        i = 0
        j = len(val) - 1
        while i < j:
            if val[i] != val[j]:
                return False
            i+=1
            j-=1
        
        return True
        