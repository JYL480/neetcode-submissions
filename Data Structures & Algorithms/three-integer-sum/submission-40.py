"""
0. Lets just keep dping this LOL. 
Today I will recap some of my thingys?? IDK
- Myabe I will recap some of myabe the stats one? IDK we will see on some other list?
- But todau we will go through 4 sum and LRU and 3 Sum again yah

4. This is 2 pointer question
- You will have to check for duppllicates for the first and second element
- soo yah


"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        n = len(nums)

        for i in range(n - 2): # Why my 2, becasuse we need to have 2 reaminig one yah to move l and
            # I will cehck for dups first

            if i>0 and nums[i] == nums[i-1]:
                continue

            l = i + 1
            r = n - 1


            while l < r:
                # Then you will do the 2 pointer, to check if the sum == 0 
                t_sum = nums[i] + nums[l] + nums[r]

                if t_sum == 0:
                    res.append([nums[i] , nums[l] , nums[r]])

                    # Here you would need to chek for the dup if there is move the l up 

                    while l < r and nums[l] == nums[l + 1]:
                        l += 1

                    l +=1 
                    r -=1

                elif t_sum >0 : # meaning too large ,we will mveo r down
                    r -=1
                else:
                    l+=1
        return res










