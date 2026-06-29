class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = set()
        resLen = 0
        l, r = 0, 0
        while r < len(s):
            if s[r] not in res:
                res.add(s[r])
                resLen = max( resLen , r-l + 1 )
                r += 1
            else:
                res.remove(s[l])
                l += 1 

        return resLen
                



        