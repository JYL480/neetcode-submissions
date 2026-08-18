"""
0. 4sum question, maybe you would need, ,nested for loop for the first 2,then have l and r pointers for the last 2
- we would need to sortye this, likely will be )n^3)



4. So will have 2 for loop fir 
then a while loop for the 3ed i guess

"""



class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []   
        nums = sorted(nums)

        n = len(nums)

        for i in range(n - 3):

            # Then you do yours thingy here
            if i >0 and nums[i-1] == nums[i]:
                continue


            for j in range(i + 1, n - 2): # I think its like that?, you need 2 left for you l and ri
                                # 2nd and 2nd prev????
                if j >i + 1 and nums[j-1] == nums[j]:
                    continue

                

                l = j + 1
                r = n - 1

                while l < r:

                    t_sum = nums[i] + nums[j] + nums[l] + nums[r]

                    if t_sum == target:
                        res.append( [nums[i] , nums[j] , nums[l], nums[r]])

                        # Or you can check 


                        while l < r and nums[l] == nums[l+1]:
                            l +=1
                        while l < r and nums[r] == nums[r-1]:

                            r -= 1
                        # Then you have l and l prev and r and r pre
                        l += 1
                        r -=1
                        
              

                    elif t_sum > target:
                        r -= 1
                    elif t_sum< target:
                        l += 1
        return res

                # 1st and 1st prev?


