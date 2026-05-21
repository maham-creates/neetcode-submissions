class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic_str = defaultdict(list)
      
        for string in strs:
            count = [0] * 26
            for c in string:
                count[ord(c) - ord('a')] += 1
            dic_str[tuple(count)].append(string)
      
        return list(dic_str.values())

        