class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if (len(s1) > len(s2)):
            return False
        S1charCount = [0] * 26
        for i, n in enumerate(s1):
            S1charCount[ord(n) - ord('a')] += 1 

        L,R = 0, len(s1) - 1
        while R < len(s2):
            S2charCount = [0] * 26
            for i,n in enumerate(s2[L:R+1]):
                S2charCount[ord(n) - ord('a')] += 1
            if (S1charCount == S2charCount):
                return True
            else:
                L += 1
                R += 1
        return False