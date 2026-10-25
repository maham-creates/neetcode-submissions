class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        from collections import defaultdict

        grouped_dict = defaultdict(list) # defaultdict for putting words together with same array.

        for word in strs:
            count = [0]*26
            for c in word:
                count[ord(c) - ord('a')] += 1
            grouped_dict[tuple(count)].append(word)
        
        return list(grouped_dict.values())







        