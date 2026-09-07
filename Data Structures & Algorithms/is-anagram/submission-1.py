class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sList = list(s)
        tList = list(t)
        sList.sort()
        tList.sort()
        return True if sList == tList else False