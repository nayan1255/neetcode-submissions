class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * (len(nums))
        
        # First pass: Calculate prefix products (left to right)
        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
            
        # Second pass: Multiply by postfix products (right to left)
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]
            
        return result
