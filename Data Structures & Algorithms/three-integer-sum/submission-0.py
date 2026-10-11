class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # FIX 1: Sort the numbers so your two-pointer logic actually works
        nums.sort()
        
        i = 0
        result = []
        while i < len(nums) - 2:  # Optimized boundary
            # FIX 2: Skip duplicates for the first element 'i'
            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue

            j = i + 1
            k = len(nums) - 1
            while j < k:
                val = nums[i] + nums[j] + nums[k]
                target = 0
                
                if target > val:
                    j += 1
                elif target < val:
                    k -= 1
                elif target == val:
                    result.append([nums[i], nums[j], nums[k]])
                    
                    # FIX 3: Move BOTH pointers to break the infinite loop
                    j += 1
                    k -= 1
                    
                    # FIX 4: Skip duplicate values for 'j' and 'k'
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
            i += 1
        return result
