"""
0. ?? IDK logn 

1. ques want to return an int which is the index
- if does note xist any then return -1 
- This has to be done in logn timing yah
- Oh the input array is sorted, 
- Binary seach


4. I dont know how to binary search LOL

This shit is aldy sorted yah. 
Just to take note hor

"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 
        r = len(nums) - 1

        while l <= r:

            half = (r + l) // 2
            print(half)
            
            if nums[half] > target:
                r = half - 1
            elif nums[half] < target:
                l = half + 1
            else:
                return half
        return -1
        

