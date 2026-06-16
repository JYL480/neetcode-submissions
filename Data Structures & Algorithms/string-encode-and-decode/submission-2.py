"""
1. have 2 functions
    - Convert a list of strings to stirings
         ["Hello","World"] = "HelloWorld" ? maybe can split them apart hor
    - Convert string back to the og list
        - Convert back to their og list

- Look at the return type yah

2. Edge cases?
    - When there is nothing? To input.

3. Naive?
- Urm 

4. There is a patter here,
- But the way to do will be to have delimiter for this!! What does this mean? Delimiter to numerb and a delkmiter 

"5#Hello5#world"
- Then when you for loop you know where to extract ig

5. Time?
    - There will be for loop for this first O(N + N) I amssuing
    - Space -   Length of the list stored O(N)

"""


class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for string in strs:
            length = len(string)
            encoded_string += str(length) + "#" + string
        return encoded_string

    def decode(self, s: str) -> List[str]:
        res, i = [], 0 
        while i < len(s):
            j = i 
            while s[j] != "#":
                j +=1
            # print(s[i:j])
            length = int(s[i:j])
            # print("ere",length)
            res.append(s[j + 1: j + length + 1])
            # print(res)
            
            i = j + length + 1

        return res


            


        
