class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp = set()
        maxLen = 0
        l, r = 0, 0
        while r < len(s):
            if s[r] not in temp:
                temp.add(s[r])
                maxLen = max(maxLen, r - l + 1)
                r += 1
            else:
                temp.remove(s[l])
                l += 1
        return maxLen

