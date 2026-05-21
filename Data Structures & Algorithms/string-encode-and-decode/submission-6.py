class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "," + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        j = 0
        while i < len(s):
            i = j
            while s[j] != ",":
                j += 1
            length = int(s[i:j])
            j += 1
            i = length + j
            res.append(s[j:i])
            j = i
        return res
            
