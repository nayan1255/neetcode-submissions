class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # Pointers for the end of valid elements in nums1 and nums2
        i = m - 1
        j = n - 1
        # Pointer for the very end of nums1 where elements are placed
        p = m + n - 1
        
        # Compare elements from the back and move the larger one to position p
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[p] = nums1[i]
                i -= 1
            else:
                nums1[p] = nums2[j]
                j -= 1
            p -= 1
            
        # If there are remaining elements in nums2, copy them over.
        # (Remaining elements in nums1 are already in their correct places)
        while j >= 0:
            nums1[p] = nums2[j]
            j -= 1
            p -= 1
