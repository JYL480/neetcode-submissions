"""
0. Yeah ofc this is sliding window?
- Maybe I will have to use a hashMap for this??
- So we need to have some counting, so we cannmot use set() yah

1. What does this question wannt?
- To return the shortest substring of s such that every character in t inclidign dupss!!
- need to return the string if cannot find then return an emoty string 


2. edge case?
- If both are exactly the same???

3. Naive?
- Check each sub string within s that matches with t. 
- I believe this will be n ^2


4. pattern?
- hashs map 
- 2 hash maps?
- Will keep moving right until the 2nd hash map is filled up?
- ONly when 2nd hash map fills up then you will move the left one???
- In the 2nd hash map the value will be a tuple! (count, index)
- So that we can teleport the left to the next char in t
 

"""



class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":return ""
        count_t = {}
        win = {}

        for char in t:
            count_t[char] = 1 + count_t.get(char, 0)

        
        l = 0
        min_len = float('inf')
        have, need = 0, len(count_t)

        res, res_len = [-1,-1], float('inf')


        for r, char in enumerate(s):
            win[char] = 1 + win.get(char, 0)

            if char in count_t and win[char] == count_t[char]:
                have += 1
            
            while have == need:

                # We want to store the indices bah
                if ( r - l + 1) < res_len:
                    res = [l, r]
                    res_len = (r - l + 1)

                win[s[l]] -= 1
                # Then do the checking?
                if s[l] in count_t and win[s[l]] < count_t[s[l]]:
                    have -=1
                l+=1

        l, r = res

        return s[l: r + 1] if res_len != float('inf') else ""
        






















