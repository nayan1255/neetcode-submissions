class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        for _ in range(k):
            val = nums.pop(-1) 
            nums.insert(0,val)
        return nums
