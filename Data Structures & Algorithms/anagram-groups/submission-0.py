from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupAnagrams = defaultdict(list)
        for word in strs:
            groupAnagrams[tuple(sorted(word))].append(word)
        
        return [list(group) for _, group in groupAnagrams.items()]