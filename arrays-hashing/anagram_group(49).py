class Solution(object):
    def groupAnagrams(self, strs):
        from collections import defaultdict
    
        anagram_groups = defaultdict(list)
    
        for s in strs:
            key = ''.join(sorted(s))
            anagram_groups[key].append(s)
    
        return list(anagram_groups.values())
