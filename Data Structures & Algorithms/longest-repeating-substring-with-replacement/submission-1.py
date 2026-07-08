class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        temp = {}
        maxLen = 0
        l = 0
        maxf = 0
        for r in range(len(s)):
            temp[s[r]] = 1 + temp.get(s[r], 0)
            maxf = max(maxf, temp[s[r]])
            while (r - l + 1) - maxf > k:
                temp[s[l]] -= 1
                l += 1
            maxLen = max(maxLen, (r-l+1))
        return maxLen

