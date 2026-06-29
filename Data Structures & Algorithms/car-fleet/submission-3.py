"""
0. Weird fkin quesiton bruh
- What is this?
- Im honestly dk 

1. What do they want?
- You will return int, whcih is the number of car fleetswhen arriving at the target area
- Urmm okay, You prob have to do some flooring or divition based on the timing and poistion
- To count the number of steps taken to reach the target. 
- If they are equal then the will belong in the same fleet. 

2. Edge cases
- Only w car?
- IDK 

3. I can nested this shit i think
hwihc is bad

4. How do you if they are in teh same fleet?
- [[Target- position]//speed 
- This is how you calculate this shit 
- BUt then what would be the plan?
- How would i do this in a singel pass?  

- This is a mmonoto stack type of question also?
- We will sort, so that we can car by car
- if we sort in descdingi position, the nearest one wpuld have to ccare abot other position car
- the furtherst one can 


"""

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pos_speed = {}

        for i, pos in enumerate(position):
            pos_speed[pos] = speed[i]
        new_dict = sorted(pos_speed.items(), reverse= True)
        print(new_dict)

        for tup in new_dict:
            print(tup)
            pos = tup[0]
            speed = tup[1] 
            time = (target-pos) / speed # Note this yeah

            stack.append(time)
            
            if len(stack) >=2 and stack[-1] <= stack[-2]:
                stack.pop()
        print(stack)
        return len(stack)


                










        