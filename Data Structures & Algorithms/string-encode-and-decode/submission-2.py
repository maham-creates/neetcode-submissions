class Solution:

    def encode(self, strs: List[str]) -> str:
        
        result =[]
        for x in strs:
            length = str(len(x))
            sep = '#'
            string = f"{length}{sep}{x}"
            result.append(string)
        return "".join(result)
    
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i<len(s):
            num = 0
            while s[i] != '#':
                num = num*10 + int(s[i])
                i += 1
            i+=1
            string = s[i:i+num]
            result.append(string)
            i += num
        return result

            
                



