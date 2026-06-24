"""

0. First instinct that this would be 2 pointers done in a single pass..

1. They want to treutnr a bool yeah, if the thing is a palnidrome


"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0 
        r = len(s) - 1
        s = s.lower()
        
        


        while l < r :
            if not s[l].isalnum():
                print("ASD")
                l+=1
                continue
            
            if not s[r].isalnum():
                print("ASDd")
                r-=1
                continue
            
            

            if s[l] != s[r]:
                return False

            else:
                l+=1
                r-=1

        return True 
            
            # So if it is not alpha numb the you will skip


 







