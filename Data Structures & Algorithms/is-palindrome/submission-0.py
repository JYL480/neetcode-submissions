"""
0. Immediate intuition
- We will use 2 pointers one starting from the front 
- Another from the back ad compare. 
- This pointers wil pass through in ta singel pass then haev some conditions...


1. What they want?
- You will return bool, if the sentence or word is a palindrome
- This can be both alpha numeric yah
- this is case insneitive, so you would prob how to make it unifom yah

2 Naive?
I guess you can reverse the stringn then ==, that can be, buut i think, you would have to 
- convert to list, themm on neach word ::-1?


3. Pattern 
- We need to normallise the sentence first. Removing the trailingn, lowercase
- Then we will use 2 ppointeers to checl

4. Complexity
- O(n)
- O(N)

"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_string = ""
        # To clean 
        for char in s:
            if char.isalnum() and char != " ":
                clean_string += char
        clean_string_norm = clean_string.lower()
        print(clean_string_norm)

        left = 0 
        right = len(clean_string_norm) - 1

        while left<right:
            # expand left 
            if clean_string_norm[left] != clean_string_norm[right]:
                return False

            left +=1
            right-=1
                
        return True
        # norm_s = s.lower()
        # no_space_norm_s = norm_s.split(" ")
        # combine_back_sting = "".join(no_space_norm_s)
        # print(combine_back_sting)








