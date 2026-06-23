"""
0. 2 pointer, but i dont know hwo to do 

1. What they want?
- they wan to retrun the number of blocks of wahter you can store 
- return an integer. 
- So you sweep the list and count the number of blocks they can add up tgt


2. edge cases?
- All the hegith 0, meaning cannot store water at all, then return 0

3. naive?
- Ig you can nested for loop this shit. 
- O(N^2)

4. Pattern?
2 pointer, 
i need to find how do i determine oh now i can store water condition.  


"""


class Solution:
    def trap(self, height: List[int]) -> int:
        # Okay wtf jy, LOL if you want to store the thing after then just populate the thing after loh
        before_list = []
        max_b = 0
        

        for num in height:
            before_list.append(max_b)
            max_b = max(max_b, num)

        after_list = [0]*len(height)
        max_a = 0 
        
        for index in range(len(height)- 1, -1,-1):
            # I need to create a moat right, if the current is more than the affter max then equate to 0 
            
            after_list[index] = max_a
            if height[index] > max_a:
                after_list[index] = 0
            max_a = max(max_a, height[index])
        # print(after_list)



        count = 0   
        for i in range(len(height)):
            cal_height = min(before_list[i], after_list[i]) - height[i]
            if cal_height < 0:
                continue
            count += cal_height
        return count




        
