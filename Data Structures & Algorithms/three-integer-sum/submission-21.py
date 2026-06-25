"""
0. Array question, and likely will be using 2 pointers, with a singular anchor at the start
- Hmm if you want to use 2 pointers you prob woudl have to sort this so that I know right side will not be 
anythign etc......
- I think this question will be O(N^2) bops
- Also this makes sense, if you are sorted, the first element will immediately determine the order you have aldy
- So if you have - 1 at the start, aso check that the next also isnt a duplicate

1. What they want?/


4. Pattern, this is very important yeah
- okay definetly we will be using a 2 pointer for this, but we have to attack the duplicates!!!!

- What does this mean?
- You have understand fully the checking of dupllicates yeah
- 1 and 2nd element we have to do the checks because if 1 + 2 aand 1 + 2, 4rd elemnt has to be -3 for it to be same 

- You have to make sure duplicates are worked on twice yeah 

- but we can the first the same, and subsequenty diff, thats why after we get t_sum == 0 
, then we will do the while tloop to check for duplcates with moving the l yeah


"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        print(nums)
        res = []

        for i, num in enumerate(nums):

            l = i + 1
            r = len(nums) - 1
            # Here will do the first cehcing yeah 
            if i > 0 and nums[i- 1] == num:
                continue

            while l <r:
                t_sum = nums[l] + nums[r] + num
                

                if t_sum == 0:
                    # Then you will append????
                    res.append([nums[l], nums[r], num])
                # Then here will heck the 2 nd anchor???
                    l+=1 
                    while l<r and nums[l] == nums[l-1]:
                        l+=1

                
                # Then here will be the moving of l and r
                if t_sum <0 :
                    l +=1
                elif t_sum >0:
                    r -=1

        return res

        