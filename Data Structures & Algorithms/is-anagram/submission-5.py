"""

1. return bool, if the 2 separate strings have same characters regardless of the order

2. Edge cases? When Both same letter? Then true

3. Naive?
    - Use a nested for loop for this

4. Bottleneck
    - Time complexity too long

5. Simple pattern? 
    - You can create a counter with a dict? then see if the counter is the same for both?
    - I will for loop twice for each word lenght, So it will be n + m, O(n + m) then 
    - O(n + m) as well to stor the counter in the dict?



"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s, count_t = {}, {}
        
        for index in range(len(s)):
            # Yeah make sense, its not +=, it will always += 1 
            count_s[s[index]] = 1 + count_s.get(s[index], 0)

        for index in range(len(t)):
            count_t[t[index]] = 1 + count_t.get(t[index], 0)

        return count_s == count_t
 
