
"""

0. Form what I rmb tbis one yha have to just rmb 

- Using the slow and fast pointer, get to the point where they meete first

- Then Another pointer from the start and that sow pointer fro the previous will meet at the duplciatae thingy

- I think

"""

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]] #.next.next, the fast pointer jumps twice

            if slow == fast:
                break

        print(slow)
        newp = 0 

        while True:
            newp = nums[newp]
            slow = nums[slow]

            if newp == slow:
                return newp
        

        