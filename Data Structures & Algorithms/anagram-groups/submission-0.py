class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list) # uses array as key in the hashmap to group the strings
        
        for strings in strs:
            alpha_count =[0]*26
            for char in strings:
                index = ord(char.lower()) - ord('a')
                alpha_count[index] += 1
            # in python list cannot be keys
            result[tuple(alpha_count)].append(strings)
        return list(result.values())
        

        


