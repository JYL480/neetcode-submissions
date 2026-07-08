"""

0. Sliding window
Oh but idk what tech i want to use on this????

1. Sliding window to get the max valueon each window?
- want to return a list

2. Edge cases?
- All the same value
- Return that value?

3. Naive?
- You can do it in n^2 using max() in the list


4. Pattern?
- WE can use deque for this or deck 
- Deck is good because time complexity to remove left and  right will be O(1) so its gicchi



"""

from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque() # Here will contain only indices yah
        output = []
        l = r = 0
        # These 2 will represent our window 
        # l will be the starting of each range, r will just keep moving loh
        while r < len(nums):


            # What do i add to the q?
            
            # But then we will pop out anu=ythnit ghat is maller with pop() fromt he righ 
            while q and nums[r] >  nums[q[-1]]:
                q.pop()
            q.append(r)

            # If the l move up then you will popleft()
            if l > q[0]:
                q.popleft()

            # Then how do we move l and r
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
        
        
            r += 1

        return output






