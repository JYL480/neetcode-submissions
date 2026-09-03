"""

0. What is this? Intuition?
- It has to be contiguois permuation yah
- Firstly i can thinnkn of having 2 hash maps to count and see whether they are equal to each pther
- Note that this wants contiguous thing, so best will be haveing a sliding windw for htis?



4. WHat is  the pattern


"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        h1 = {}
        h2 = {}

        for char in s1:
            h1[char] = 1 + h1.get(char, 0)

        l = 0
        n = len(s1)

        for r, char in enumerate(s2):

            
            h2[char] = 1 + h2.get(char, 0)
            
            while (r - l + 1) > n:
                # we will remove the left thingy 
                print(s2[l])
                # del h2[s2[l]] Oh this - the whole thing, i just want - = 
                
                h2[s2[l]] -= 1
                if h2[s2[l]] == 0:
                    del h2[s2[l]]

                l += 1



            # Then we will do the cehcking here 
            # We we will current and check
            if h2 == h1:
                return True

        return False


        