"""


# Let's recap with a sliding windin type shit bah. 
Or shouold i recap the thing that i did????
0. First thing, my initiontion to use sliding window. 
- In sliding window you will have to move l and r pointer. 
l when the while loop cindition failes
r whe it is okkay loh

1. What does the question wat?/
retunr the len, whihc is an int
- The length of the lngest substrinig
- Not dups. 


3. Time complexity 
O(N)
space: O(1)

4. How to do it?
- Use a hash map to track 
- Then if there is dup, you will track then move L u.   



"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = r = 0
        max_len = 0

        seen = set()
        
        for r, char in enumerate(s):

            # Dafuq you didnt even use your L or R
            while seen and char in seen:
                
                seen.remove(s[l])

                l +=1
            #Then you will add here bah

            seen.add(char)

            max_len = max(max_len, (r - l) + 1)
            

        return max_len











        