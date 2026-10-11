class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        # 'i' tracks the index of the last unique element found
        i = 0 
        
        # Loop through the list starting from the second element
        for j in range(1, len(nums)):
            # If we find a new unique element
            if nums[j] != nums[i]:
                i += 1          # Move the unique pointer forward
                nums[i] = nums[j]  # Update the array in-place
                
        # The number of unique elements is i + 1 (since index starts at 0)
        return i + 1
