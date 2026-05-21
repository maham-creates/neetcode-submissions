class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashset = defaultdict(list)

        for string in strs:
            count = [0]*26
            for i in string:
                count[ord(i) - ord('a')]+= 1
            
            hashset[tuple(count)].append(string)
            print(hashset)

        return list(hashset.values())



        
     