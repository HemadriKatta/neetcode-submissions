class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_map = {}
        t_map = {}
        maxLen = max(len(s), len(t))
        for x in range(maxLen):
            s_map[s[x]] = s_map.get(s[x], 0) + 1
            t_map[t[x]] = t_map.get(t[x], 0) + 1
        return s_map == t_map
        