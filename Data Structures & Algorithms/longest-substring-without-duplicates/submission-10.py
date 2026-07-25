"""
0. First instinct, that they want a sub string from the string
- a sub string 
meaning that they want to a sliding window type shit!!

1. What do they want?- Tthey want to find the longest substring without dup 
- Then you will return the len of the sub string

skip

4. Pttern?
- SLiding widnow ts
-  We must know what are the conditions to move left
move left until the substring is a proper string 
- left and right to calculate the len 

5. Complexity 
- Time - O(N)
- Bcos we are trying to do it in a single pass
- Space - Idk yet 



"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        

        l_i = 0 
        max_len = 0 
        seen = set()

        for r_i, char in enumerate(s):
            
            while seen and char in seen:
                # I will only cal the len after removing the char that is seen
                seen.remove(s[l_i])
                l_i +=1

            seen.add(char)
            max_len = max(max_len, r_i - l_i + 1)
        return max_len













        