"""
0. what 

1. return list of list of overlapping 
- Hmm Array and soritn huh


def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    res = []



    intervals.sort(key=lambda x: x[0])

    l = intervals[0][0]
    r = intervals[0][1]


    for newl, newr in intervals[1:]: # huh okay I was wondering how to do this
        if newl <= r:
            r = max(r, newr)
            # l still teh same
        else:
            res.append([l, r])
        
            l = newl
            r = newr
            
    # That means you are the lest one aldy
    res.append([l,r])
    return res

"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        res = []

        l, r = intervals[0]

        for newl, newr in intervals[1:]:
            if newl <= r:
                # Then we have new r
                r = max(newr, r)
            
            else: # Diff segment
                res.append([l,r])

                l = newl
                r = newr
            
        res.append([l,r])
        return res











