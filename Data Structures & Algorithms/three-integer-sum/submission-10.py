"""

0. It is a 2 pointer question, and this is without sorted. 
- WE can work with sorted. From what i rmb, there is only O(N^2) solution to this

1. What they want?
- They want you to return a list of list which containes distnace indices of the added targets tgt. 
- All of them must equate to 0


Skipppp

4. Pattern, this will be a 2 pointer
- Take note that the the first item in the sub list determines the subsequent values in teh list. 
- So if you ahve thee same elements, then skipp yeah. 
- Also doing withn the cahngeing of the pointers within the increments and decrement in pinters 
- answer can leasd to duplicate a s well? 

- becuase it didnt return, but it can another set of answer with the same starting initial unumbers




"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # From teh start, you can have  duplicate yeah
        res = []
        nums = sorted(nums) 
        # print(nums)
        
        for i, num in enumerate(nums):
            # Right now at teh start, if you have a have precious same number, youi will have the same asnwer
            if i >0 and num == nums[i-1]:
                continue
            
            l = i +1 
            r = len(nums) - 1

            while l <r:
 
                t_sum = num +  nums[l] + nums[r]
                # print(num,nums[l], nums[r],t_sum)

                # You can add first?, but with the l and r movement tehre can be duplicates such atht if its the same l will give the same results


                if t_sum == 0:
                    res.append([nums[l], nums[r], num])
                    l+=1
                    # print(res)
                    while nums[l] == nums[l-1] and l<r:
                        l+=1
                elif t_sum > 0:
                    r-=1
                elif t_sum <0:
                    l+=1


        return res
  

            

        