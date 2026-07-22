"""
0. What is  your intuition?\
- Choose up to k characters to replace them?
- with upper case 
- Yeah this is sub set of the string, liely we will ussliding window of some sort
- Slding window you are using some pointers as well, only when the your condition is not valid athen yo
- expand or something 




4. You need to kwnow aht is the passing condition for shifting l pp=oinitner

- I need to find what is the max char in that sqyuenc


"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0 
        max_len=0 
        hash_char = {}
        
        for r, char in enumerate(s):

            hash_char[char] = 1 + hash_char.get(char, 0)
            
            maj_len = max(hash_char.values())
            


            #  here will be the invalid condition to move l up 
            while hash_char and ((r - l + 1) - maj_len) > k:  
                print((r - l) - maj_len)
                hash_char[s[l]] -= 1 

                l +=1 
            print(hash_char)
            
            
            # If not in valid, which is outside, then you will max_len here?
            max_len = max(max_len, (r-l + 1))
            
        return  max_len


    















