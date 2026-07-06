"""

0.What is this? THis can be sort of a sldinf window ts with 2 sets and count for this


4. YOu will compare with 2 hashmaps, and then the other will be -1 or del off yah



"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        h_s1 = {}
        h_s2 = {}
        len_s1 = len(s1)

        for s in s1:
            h_s1[s] = 1 + h_s1.get(s, 0)
        
        l = 0 
        
        for r, char in enumerate(s2):
            # Will populagte the s2
            h_s2[char] = 1 + h_s2.get(char,0)

            # Now if the longer than you will left up del or -=1
            # only after I move up then I will check

            while (r - l + 1) > len_s1:
                h_s2[s2[l]] -= 1
                if h_s2[s2[l]] == 0:
                    del h_s2[s2[l]]
                l +=1

            if h_s1 == h_s2:
                return True
        
        return False
            

            
 


        