"""
0. Iniuition?
- sub string, then it will be using a sliding window method LOL

- What does this mean?
- Meaning you will have 2 pointers, and you will keep exapnding right
- Only with some condition then you move l up



4. What is the pattern?
- You will l and r popintner
- If the that current letter is in the seen set() ig, then you will move the l up.....
- Else move up r

- This iwll be done in a single pass



"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0 
        
        max_len = 0 

        seen = set()

        for r, char in enumerate(s):
            # I want to remove first then append

            while char in seen:

                seen.remove(s[l])
                l+=1

            seen.add(char)
            llen = r - l + 1
            max_len = max(llen, max_len)
            print(seen)
            print(max_len)
        return max_len












        