"""
0.  Major hind, this is sorted ascedinging
- Maybe have to do some searc
- Need to finnd out how it was roated, where tits the last and first?
- Its only rotated if the last item is < then list[0]
- 

1 . return th emsalles element in the list in log n time when the list is rotates

4. How to do it?
- Because its roated, so there will be ean infelelction point where there will be 2 sorted segments in the thing
- will always cehck left

for the mid, then you got to find a condition to decide which sortyed left or right sgemet you want to seach 
- Both are sorted aceding order yah 

- nnums[m] >= nums[l]:
meaning the, we search on the right side, then it will be the ormal condition ?
- If not search left

- Once you are there then you do the binary search 

"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r= 0, len(nums) - 1
        min_val = float('inf')
        

        while l <=r:
            if nums[l] < nums[r]:
                min_val = min(nums[l], min_val)
                break
           
            mid = (l + r) //2
            
            min_val = min(nums[mid], min_val)
            
            if nums[mid] >= nums[l]: #meaing that ew have to search right side, is smaller for us
                l = mid + 1
            elif nums[mid] < nums[l]:
                r = mid - 1
        
        print(min_val)
        return min_val