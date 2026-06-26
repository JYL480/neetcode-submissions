"""
OKay lemme do again yah, so that i know about the default dict 
"""

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_map = defaultdict(list)
        re_list = []
        
        # Now that I have a dict, i will sort the words and that will be the key

        for string in strs:
            sorted_string = "".join(sorted(string))
            
            ana_map[sorted_string].append(string)
            # print(ana_map)

        for k, v in ana_map.items():
            re_list.append(v)

        return re_list








