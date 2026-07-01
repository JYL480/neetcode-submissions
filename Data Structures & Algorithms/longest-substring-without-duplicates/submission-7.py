"""
0. We will look nto more in depth question yah
Moving on the sliding window ts???

- When they askk for sub string?? Meannig with a sub thingy, when we want a sub thingy, this means we want 
sliding window??? IDK

1. What do they want?

- They want to return the len of the sub string within the syting that does not have duplicate]
- return value must be an int 
- Longest sub string!!!!!!


2 Edge case?
- When all is diff
    - Then will  be the length

- When all the same?
    - Return 1
- when you have nothing
    - Return 0 ig

3. Naive?
- Urm I guess youy can do nested one loh which is bad....

4. Pattern?
- Ofc this would be a sliding window, as they wna  t a sub string for this yah

- so startingn with a sub string, maybe a list or jsut string 
- If the condition is right, then expand, if the condition is bad than subtract from the lefet???

- This will be done in a single pass ig



"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0 
        # have a seen dict? or set?

        seen = set()
        max_len = 0  
        substring = []

        for r in range(len(s)):
            
            while s[r] in seen:
                seen.remove(s[l])
                l+=1
            seen.add(s[r])
            max_len = max(max_len, (r - l) + 1)
        return max_len
            
            
            













        