class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mp = {} # Track state
        maxfreq = 0
        replacements = 0
        max_length = 0
        L = 0
        for R in range(len(s)):
            mp[s[R]] = mp.get(s[R], 0) + 1
            maxfreq = max(maxfreq, mp[s[R]])
            replacements = R - L + 1 - maxfreq
            if replacements > k:
                mp[s[L]] -= 1
                L +=1
            else:
                max_length = max(max_length, R-L+1)
        return max_length
            