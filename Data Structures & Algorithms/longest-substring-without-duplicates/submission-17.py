"""
0. Lets do some warm up yah 
- find the longest supstring
- Note that we see that it is contiguois!!! THis means sliding window liao
- Note that we wannt contiguous so this is important yah


1 .What they want to they want the largest substring contigouuys!!!



4. WIl be a sliding wiindow!!
- You will have seen hash set which coutnts, and not a set() yah because you cannot count that shit HOHO
- URMMM when the the count of etierh is more than >1 then you move left up or soemthing 
- IDK we will see



"""



class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 
        seen = set()
        max_len = 0

        for r, char in enumerate(s):
            # Rmb that sliding window is a variation of 2 pointers, adn they are movinf in the same direction!!
            while s[r] in seen:
                
                # Then we willl remove 
                seen.remove(s[l])
                l += 1
            
            seen.add(char)
            
            max_len = max(max_len, (r - l) + 1)

        
        return max_len


