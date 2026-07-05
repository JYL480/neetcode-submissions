"""
0. Substring again, 
- Find a sub sring that is can satisfy this condiiton
- Meaning it will be a sliding window IG

1. What doed the question want?
- How Return the len of the longtest sub string that can have replacemnet loh 

- You only have k number of times for replacement

skip

4. Sliding window with this shit

- Prob will have a hash map with the mex count???
- Then you have l and r sliding window for this



"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hash_map = {}


        l = 0
        max_len = 0


        for r, char in enumerate(s):
            
            hash_map[char] = 1 + hash_map.get(char, 0)
            maj_char = max(hash_map.values())
            print("maj",maj_char)

            while hash_map and ((r - l + 1) - maj_char) > k:
                print(l,r)
                # When the remaining miniory is more than K then Ii will remove l char from the hash_map
                # Then move l up

                hash_map[s[l]] -= 1
                l +=1 
                print((l - r + 1))
            max_len = max(max_len, (r - l + 1))

        return max_len
            
            # Only after you remove all the thign you want
            # Then yoi will find the len?????
















