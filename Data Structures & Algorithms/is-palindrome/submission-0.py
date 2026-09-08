class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s = "".join([c for c in s if c.isalnum()])
        for i in range(0, len(cleaned_s), 1):
            rightPointer = len(cleaned_s) - i -1
            if(not(cleaned_s[i].isalnum()) or 
            not(cleaned_s[rightPointer].isalnum())):
                continue
            if cleaned_s[i].lower() != cleaned_s[rightPointer].lower():
                return False
        return True