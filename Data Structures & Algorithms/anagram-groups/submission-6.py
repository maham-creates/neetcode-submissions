class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        grouped = defaultdict(list)

        for string in strs:
            count = [0] * 26
            for c in string:
                count[ord(c) - ord('a')] += 1
            grouped[tuple(count)].append(string)

        return list(grouped.values())

            
        