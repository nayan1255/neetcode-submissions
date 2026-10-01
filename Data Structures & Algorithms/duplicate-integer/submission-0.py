class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        val = set()
        for x in nums:
            if x in val:
                return True
            val.add(x)
        return False