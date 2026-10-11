class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m - 1
        j = n - 1
        p = m + n - 1

        while 0 <= i and 0 <= j:
            if nums1[i] > nums2[j]:
                nums1[p] = nums1[i]
                i-=1
            else:
                nums1[p] = nums2[j]
                j-=1
            p-=1
        
        while 0 <= j:
            nums1[p] = nums2[j]
            j -= 1
            p -= 1


