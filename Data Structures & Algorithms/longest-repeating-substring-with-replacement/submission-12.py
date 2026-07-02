"""
0. Sub string, most likely will be a sliding window ts yeah




4. Pattern?

- You need to know what is the moving condtion
- When the len of the string inside - mojaoirty of the words >= target, then you will move the thingy
- 



"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        c_hash = {}

        l = 0 
        max_len = 0 

        for r in range(len(s)):

            c_hash[s[r]] = 1 + c_hash.get(s[r], 0) 
            max_k = max(c_hash.values())

            
            while ((r - l + 1) - max_k) > k :
                c_hash[s[l]] -= 1

                l += 1



    
                print(c_hash)
            
            max_len = max(max_len, r - l +1 )
            print(max_len)

            # while #This while loop will be to move left until condition met 

        return max_len
            # here I will append?
        
        