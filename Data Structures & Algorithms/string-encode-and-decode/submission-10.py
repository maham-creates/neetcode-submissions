class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s))+"#"+s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i,j = 0,0
        while i < len(s):
            num = ""
            while s[i] != "#":
                num += s[i]
                i += 1
            length = int(num)
            i += 1
            j = i + length
            res.append(s[i:j])
            i = j
        return res


