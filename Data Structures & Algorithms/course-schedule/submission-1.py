"""
0. Saem field as the island thingy yah 



1. Return bool for this!


4. We have to check whether there is no loop within this thing!!
- DFS recursion on this shit yah 
- we will use a hash map with their jumps
- We will use a vist set() as well this see if they have been visited, if we see it has aldy been visited, means a loop, then will return false

"""

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        
        mapping = {i:[] for i in range(numCourses)}
        # Oh the mapping inside is a list uh 
        seen = set()    

        for c, p in prerequisites:
            mapping[c].append(p)


        # Okay now we got the list we will porb the dfs here

        def dfs(c):
            # Like all the dfs, same thing as the island, if we have visited htis, means tehre is a loop return false
            if c in seen:
                return False

            if mapping[c] ==[]: # Meanign there we are in an emty rlist
                return True

            seen.add(c)

            # Then we will use the global thingy for this yah hoh oh ho ho hh h 
            for pre in mapping[c]:
                if not dfs(pre):
                    return False

            # Now to mark that we have visted, make sure is not in the seen beacuse see that is seen means a cyle
            seen.remove(c)
            
            # Now to do some DP kinda thing, we know c is correct no matter we dont have to run the thing again 
            mapping[c] = []
            return True

        # Now to count, we hav edge case. maybe we have 2 irreducuble graph or something 
        for c in range(numCourses):
            if not dfs(c):
                 return False

        return True
        
        
        
    