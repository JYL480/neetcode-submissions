"""
1. So we want to group all the anagram in a sublist from a full list, 
- Have to return a nested list
- Anagram just needs to contain the same letters thats all yah

2. Edge cases?
    - When you have nothing yah, then return a nest list of nothing

3. Naive?
    Triple nested for loop?

4. i will convert all the index strings to counts with a dict 
- Then another separate loop to group them tgt?
- So will have nested for loop at the start? O(N*longest word) + O(N), the second will be to loop

"""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        
        ana_map = {}
        re_list = []

        for s in strs:
            # print(sorted(s))
            sorted_str = "".join(sorted(s)) 
            # print(sorted_str)
            ana_map[sorted_str] = ana_map.get(sorted_str, [])
            ana_map[sorted_str].append(s)
            
        for k,v in ana_map.items():
            re_list.append(v)
        return re_list
            






