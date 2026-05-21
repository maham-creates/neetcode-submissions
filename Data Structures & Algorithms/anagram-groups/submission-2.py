class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashtable = defaultdict(list)

        for string in strs:
            count = [0]*26
            for i in string:
                count[ord(i)-ord('a')]+=1
                # .append used because its a list
            hashtable[tuple(count)].append(string)
        
        return list(hashtable.values())
        
        

        