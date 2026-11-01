class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "&" + s
        # 5&Hello5&World
        return res

    def decode(self, s: str) -> List[str]:
        
        i = 0
        res_str = ""
        res = []

        while i < (len(s)):
            str_num = ""
            while s[i] != "&":
                str_num += s[i]
                i += 1
            len_num = int(str_num)
            i += 1
            res_str = s[i:i+len_num]
            res.append(res_str)
            i += len_num 
            
        return res

                 
