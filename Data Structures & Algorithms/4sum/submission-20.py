"""
0. Lets try this agian, yah you should be able to do this!!!

- Using nested for loops with a converging pointer

- also note that converging pointer mist of the timme you need to sort 

- should be gucci


4. lets just skip it yah, 
- TI thinkk it would be fine for me hor!!
- Right I think 

5. I will have a nested for loop for this shit i think! Hor!! Please take note again
So the time complexity will likely be O(N^2)


"""



class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        res = []
        nums = sorted(nums)

        for i in range(n - 3): # We will -3, because we need to leave for the next 3 nums
            if i >0 and nums[i] == nums[i -1]:
                continue

            for j in range(i + 1, n -2):  # Should be someething liek this because we are moving the next numer and leaving l and r huince - 2
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                    
                l = j + 1
                r = n - 1

                while l < r:
                    t_sum = nums[i] + nums[j] + nums[l] + nums[r]
                    if t_sum == target:
                        res.append([nums[i], nums[j] , nums[l], nums[r]])

                        while l<r and nums[l] == nums[l+1]:
                            l += 1

                        l +=1 
                        r -= 1

                    elif t_sum > target:
                        r -=1

                    elif t_sum < target:
                        l += 1

        return res




