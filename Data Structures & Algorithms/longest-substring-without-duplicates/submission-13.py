# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         l = 0
#         charSet = set()
#         maxLength = 0
#         for r in range(len(s)):
#             while s[r] in charSet:
#                 charSet.remove(s[l])
#                 l += 1
#             charSet.add(s[r])
#             maxLength = max(r-l + 1, maxLength)
#         return maxLength

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        l = 0
        res = 0

        for r in range(len(s)):
            if s[r] in mp:
                l = max(mp[s[r]] + 1, l)
            mp[s[r]] = r
            res = max(res, r - l + 1)
        return res