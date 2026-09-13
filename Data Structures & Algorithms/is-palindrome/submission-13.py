"""
0. Wtf is this" What is a palindrom
- When the wrods are the same backwards and forward, 
- Meaning, you will rteurn a bool value 
- Intuition, if you want to want to work from tghe back ad front, is a 2 pointer 


1. the questyion wants you to return a bool value, ig its  boo


4. l = 0

- I need to know the condition to move both 
- Are the movinga thte same time?
- Yeah moving at the same time

- Holfy fk why got somehing wan


"""


class Solution:
    def isPalindrome(self, s: str) -> bool:

        l = 0 
        r = len(s) - 1
        s = s.lower()
        print(s)
        
        while l<r:
            
            if not s[l].isalnum():
                l+=1
                continue
            
            if not s[r].isalnum():
                r -=1           
                continue 
            print(s[l], s[r])    

            if s[l] != s[r] :
                return False
                
            

            l += 1
            r -=1

        return True







