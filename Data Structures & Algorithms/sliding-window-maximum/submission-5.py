"""

0. This is very similar this is also very similalr to the mpmontoci stacl l[[romn;
where we want the first element to be always [0] to be the largest
- Then wehen its time to reduce then you will move

4. What is th epattern?


"""

from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d = deque() # inside are the indexes yah

        res = []
        l, r = 0, 0

        for r, num in enumerate(nums):

            while d and num > nums[d[-1]]:
                d.pop()


            d.append(r) # At the new one this will be the biggestish or in teh correct spot

            if (r + 1) >= k:

                res.append(nums[d[0]])
                l +=1

            # i also have to to move remove the edge

            if l > d[0]:
                d.popleft()


        return res






