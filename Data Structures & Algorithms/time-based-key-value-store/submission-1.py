"""
0. For this question, you will have a hash map list where inside is a tuple yah, and you have to search for the next biggest for that hsit 
- Because they are done in ascending then you know we might have to do in binary search


4. Binary search with a hashlist tuple?



"""

from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.hashlist = defaultdict(list)
 

    def set(self, key: str, value: str, timestamp: int) -> None:
        # How to set?
        self.hashlist[key].append((value, timestamp))
        print(self.hashlist)

    def get(self, key: str, timestamp: int) -> str:
        # How to get 
        # We need to now how to get teh thingy we want? What is valid or not 
        res = ""

        res_time = 0 
        l = 0 
        r = len(self.hashlist[key]) - 1

        while l <= r:

            mid = (l + r)// 2 # This will be the timing I see whether have or not ir the index 

            if self.hashlist[key][mid][1] <= timestamp: # I can afford to be slower
                res = self.hashlist[key][mid][0]
                l = mid + 1
            elif self.hashlist[key][mid][1] > timestamp:
                r = mid - 1
            
        return res
        

            



            

