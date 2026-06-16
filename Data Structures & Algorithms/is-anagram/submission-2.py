"""
Understanding?
- Want to chekc whther its an anagram for this. Oops i did not undersant teh question
- mYabe i will jsut flip the string and check if thy are qya 
- LOl i assumed again. LOL 
- Just both ahve the same char, thats all

Brainstorming

Implementation

Use a conter?
- Use a dict for a counter

"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count_s, count_t = {}, {}

        # here you can populate the counter
        for i in range(len(s)):
            count_s[s[i]] = 1 + count_s.get(s[i],0) # Rmg the systax, the snd arg is the default value
            count_t[t[i]] = 1 + count_t.get(t[i],0)
        

        return count_t == count_s
 
