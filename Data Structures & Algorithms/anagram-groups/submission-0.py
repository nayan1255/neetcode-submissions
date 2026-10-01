from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Use a dictionary where the value defaults to an empty list
        anagram_map = defaultdict(list)
        
        for s in strs:
            # 1. Sort the characters of the string
            # 2. Join them back into a string to use as a dictionary key
            sorted_key = "".join(sorted(s))
            
            # 3. Append the original string to the matching key list
            anagram_map[sorted_key].append(s)
            
        # Return all the grouped sublists
        return list(anagram_map.values())