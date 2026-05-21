class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        #[0 ......26]
        char_arr = [0] * 26
        for char in s:
            char_arr[ord(char) - ord('a')] += 1
        
        for char in t:
            char_arr[ord(char) - ord('a')] -= 1

        for num in char_arr:
            if num != 0:
                return False
        return True


        


