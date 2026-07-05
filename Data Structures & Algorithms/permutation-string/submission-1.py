"""

0. Hmm i can see how this can be a slding LOL


1. What does it want?
- Will return bool true or false
- if there is a sub string in s2 which is the same as permutations in s1

2. Edge cases?
- if there is only 1 letter in s1, then if that letter is present in s2, hell yeah 

3. Naive?
- I can check every sub string in s2, by sorting tehm out first. 
- O(N^2) bah inlcuding the sorting which is nlogn 

4. Pattern
Sidingw indo?
if the current elgn is mroe than the len of s1, then will move l += 1
- Then you will cehck if in set() or not
- After moving you will do your checks

5.  Will be donw ina single pass?




"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # I will use a hash_map instead with a counter, that will be better!!
        h_s1 = {}
        h_s2 = {}
        len_s1 = len(s1)
        l = 0
        for s in s1:
            h_s1[s] = 1 + h_s1.get(s, 0)
        
        for r, char in enumerate(s2):

            h_s2[char] = 1 + h_s2.get(char, 0)

            while (r - l + 1) > len_s1:
                h_s2[s2[l]] -= 1

                if h_s2[s2[l]] == 0:
                    del h_s2[s2[l]]

                l += 1

            
            if h_s2 == h_s1:
                return True
        return False
            # I wil do the checkks here?
            

        # l = 0 
        # len_s1 = len(s1)

        # for r, char in enumerate(s2):



                







        