"""
Understanding?
- Want to chekc whther its an anagram for this. Oops i did not undersant teh question
- mYabe i will jsut flip the string and check if thy are qya 
- LOl i assumed again. LOL 
- Just both ahve the same char, thats all

Brainstorming

Implementation

Use a conter?

"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Right we can sort with strin gisit
        sort_s = sorted(list(s))
        sort_t = sorted(list(t))
        return sort_s == sort_t
 

