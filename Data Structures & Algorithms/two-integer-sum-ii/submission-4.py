class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        while i < j:
            val = numbers[i] + numbers[j]
            if target > val:
                i+=1
            elif target < val:
                j-=1
            else:
                return[i+1, j+1]