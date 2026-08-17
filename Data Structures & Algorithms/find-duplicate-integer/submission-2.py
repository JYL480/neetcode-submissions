
"""

0. Dafuq is this lol
- So using the flpyes' alo which is the fast and slow pointer
- When they first intersect distance to that pointer == Distsance from the first node 
- That is the main thing

"""

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0 

        while True: 
            # Return the interserct 
            slow = nums[slow] # Will move to the next
            fast = nums[nums[fast]]  #

            if slow == fast:
                break
        # Now slow will be at the pinter of ineterstextion
        # Will create another pointer for this yah, so that we know where to move 

        slow2 = 0 

        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow2 == slow:
                return slow2
        
