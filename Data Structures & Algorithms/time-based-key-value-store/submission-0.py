"""
1. What they want?
- Create functions which is set and get, set will return nothing, 
set will return string, of the value which is lesser than the gegt time sta-p largest timestamp_prev
- THis is the one yah


2. edge cases?
IDK


3. naive?

4. Pattern
- Hint kniwingthat the time stamp shuld be added increasingly, meanign this is sorted, we can binary serach this?
- Put a wat
- Hash map? Default dict which containes the tuple?



5. complexity
- Set() - this should be O(1)
- Get, meaning we would have to search should be lessert than o(n)


"""

from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list)
        # Key will be the name, inn th list will be tuple of the emotion and number bah
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append((value, timestamp))
        print(self.hashmap[key])


    def get(self, key: str, timestamp: int) -> str:
        
        l =0 
        r = len(self.hashmap[key]) - 1


        res = ""
        
        while l <= r:
            mid = (l + r) //2

            print(self.hashmap[key], timestamp)


            if self.hashmap[key][mid][1] <= timestamp:
                # This is valid
                res = self.hashmap[key][mid][0]
                l = mid + 1
                
            elif self.hashmap[key][mid][1] > timestamp: # this is invlalide
                # If it more than I want the mid - 1
                r = mid - 1
            
        return res

            

