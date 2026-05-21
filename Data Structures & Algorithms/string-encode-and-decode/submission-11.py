class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            res += str(len(string)) + "#" + string
        return res



    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            j = i
            length_str = ""
            while s[i] != "#":
                length_str += s[i]
                i+= 1
            length = int(length_str)
            j = i+1
            i += length
            i+=1 
            res.append(s[j:i])
        return res

