class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Create an array of all permutations of s1
        # check if substring of s2 is in s1
        if (len(s1) > len(s2)):
            return False
        S1charCount = [0] * 26
        for i, n in enumerate(s1):
            S1charCount[ord(n) - ord('a')] += 1 

        L = 0
        R = len(s1) - 1
        # for R in range(1, len(s2) - 1, 1):
        #     S2charCount[ord(s2[R]) - ord('a')] += 1
        #     if(S1charCount == S2charCount):
        #         return True
        #     else:
        #         L +=1
        print(f'S1charCount: {S1charCount}')
        while R < len(s2):
            S2charCount = [0] * 26
            newArr = s2[L:R+1]
            for i,n in enumerate(s2[L:R+1]):
                S2charCount[ord(n) - ord('a')] += 1
            print(f'S2charCount: {S2charCount} for {s2[L:R+1]}')
            if (S1charCount == S2charCount):
                return True
            else:
                L += 1
                R += 1
        return False