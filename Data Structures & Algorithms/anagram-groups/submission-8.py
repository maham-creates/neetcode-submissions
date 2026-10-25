class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        from collections import defaultdict
        result = []

        if len(strs) <= 1:
            return [strs]

        strs = sorted(strs)
        # ['act', 'cat', 'hat', 'pots', 'stop', 'tops']
        grouped_dict = defaultdict(list) # defaultdict for putting words together with same array.

        for word in strs:
            count = [0]*26
            for c in word:
                count[ord(c) - ord('a')] += 1
            grouped_dict[tuple(count)].append(word)
        
        for val in grouped_dict.values():
            result.append(val)
        
        return result







        