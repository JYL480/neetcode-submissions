"""
0. First intuition
- If they want to see the forward and backward if its correct or not. Whether this makes as a palindrom, then we will do 
a 2 pointer method yah

1. What they want?
- They want to return bool
- to check

"""


class Solution:
    def isPalindrome(self, s: str) -> bool:

        left = 0 
        right = len(s) - 1

        while left < right:
    
            left_char = s[left].lower()
            right_char = s[right].lower()
            if not left_char.isalnum():
                left+=1
                continue
            if not right_char.isalnum():
                right-=1
                continue    

            # # Will do the norm and check here?
            if left_char != right_char:
                return False


            print(left_char)
            left+=1
            right-=1
            
        return True
           

 







