"""
0. 2 pointers yah, i think this is the one

1. Return an array, the product of al lthe rest of the items except itself.....
- and you have to solve in O(n) oof.
- The elements in the array will be N^32 large.....



2. Edge cases?
     -negative number you have to deal with them yah
     - Um if only 2 numbers? Then it will be itseff ig swapped places

3. Naive?
    - Yes using the division, but no we cant use that 
    - Urmm if current index then continue? With a nested for loop bah
    Bottel neck = O(N^2)

4. Pattern?
    - 2 pointers, in a single pass?

time complexity
O(N)
Space
O(N)


"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # I think it starts like this?
        i = 0  # Will point the to the main thing 
        j = 1
        res = []
        prod = 1
        while i < len(nums):
            
            if j != i and j <len(nums): #if current pointer j !=  i, then +=1
                # do your thing
                # print(j,nums[j])
                prod *= nums[j]
                # print("prod", prod)
                j+=1
            elif j == i:
                j+=1
                continue # meaning ignore this
            else:
                res.append(prod)
                # print(res)
                prod = 1
                j = 0
                i+=1

        return res







        