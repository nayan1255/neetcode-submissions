from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        angrammap = defaultdict(list)

        for val in strs:

            sorted_val = "".join(sorted(val))
            angrammap[sorted_val].append(val)
        
        return list(angrammap.values())