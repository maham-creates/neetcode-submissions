class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = defaultdict(list)

        for strings in strs:
            count = [0] * 26
            for i in strings:
                count[ord(i) - ord('a')] += 1
            hashmap[tuple(count)].append(strings)
        
        
        return list(hashmap.values())
