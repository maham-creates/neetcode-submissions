class Solution:
    def isalphanum(self,c):
        return ((ord('a')<= ord(c) <= ord('z'))
               or (ord('A')<= ord(c) <= ord('Z'))
               or (ord('0')<= ord(c) <= ord('9')))

    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1

        while i < j:
            if self.isalphanum(s[i]) == False:
                i += 1
                continue
            if self.isalphanum(s[j]) == False:
                j -= 1
                continue
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True
            
    
