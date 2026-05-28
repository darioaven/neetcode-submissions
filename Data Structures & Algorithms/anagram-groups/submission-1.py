from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s_dict = dict()
        for s in strs:
            srt = "".join(sorted(s))
            if srt not in s_dict:
                s_dict[srt] = []
            s_dict[srt].append(s)
        return [k for k in s_dict.values()]



        