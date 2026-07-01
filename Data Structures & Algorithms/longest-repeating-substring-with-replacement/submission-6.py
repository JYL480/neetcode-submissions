"""
0. 

1. What does this question wnat?
- You will return int of the len of the longest sub sytring that only have 1 dinstinv char

- When they wan tto have asub array, we will do with some sliding window of some sort bah, 
- So it s like  2pointer, but you have window for the lelgnth which matcehs the question 


- so you can replace k chars to get a longest continous single char string.......
- and you will reutrn int lenof th elongest continus char 


2. Edge cases?
- When you have only 1 char
- return 1

3. Niave?.
- Nesteed nested nested 
- IDK 

4. Pattern?
- Slidding window with hash map to see whether the current window is valid or not
- WHat is the codndition to cehcll l
- The max char - min, Then if that value <= k, then you it is valid
- then r +=1
else l+=1






"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hash_map = {}
        

        l = 0 
        max_len = 0
        maxk = 0

        for r, char in enumerate(s):
            # Populat ethe hash map
            hash_map[char] = 1 + hash_map.get(char, 0)
            maxk = max(maxk, hash_map[char])


            while (r-l + 1) - maxk> k:
                hash_map[s[l]] -=1
                l+=1
            max_len = max(max_len, r-l +1)
        return max_len




        