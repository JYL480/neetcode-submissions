"""
0.  Okay, I each window or wa want to get what?
- So if it was a non sorted array, we want to get the max as the thing is gettingbigger
- THen we can use a monotonic stack for this 
- But we have to remove from the leeft
- So a stack and you can also remmove from the left is deque :)
- What is the deque, is a double sided queue which you can appenedleft and popleft

skip

4. Pattern?
- Using deque
- Somthing liek tha t



"""

from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d= deque() # insdie the d will be indedx to we can make easy to see whether its out of range
        res = []
        l = 0

        for r, num in enumerate(nums):

            while d and nums[d[-1]] < num: #meaning the first item must always be the biggest
                d.pop()
            # ONly after you do the while loop to ensure correct deque struct then append d
            d.append(r)
            print(d[0], l)


        
            if (r + 1) >= k:
                print(d[0])

                l+=1
                res.append(nums[d[0]])
            
                        
            if d[0] < l:
                print(d[0], l)

                d.popleft()

        return res






        




