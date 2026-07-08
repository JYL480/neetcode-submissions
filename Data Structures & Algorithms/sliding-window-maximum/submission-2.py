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

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque() # In here I will include the indices bah
        l, r = 0,0

        res = []

        while r < len(nums):
            
            while q and nums[q[-1]] < nums[r]:
                q.pop()
        
            q.append(r)

            # Here will be when out of range

            if l > q[0]:
                # Meanig out of range aldy
                q.popleft()
            
            if (r + 1) >= k:
                res.append(nums[q[0]])
                l+=1


            r += 1
        return res
        






