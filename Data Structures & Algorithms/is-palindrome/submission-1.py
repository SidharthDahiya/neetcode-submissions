class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        left = 0
        rigth = len(s) - 1

        while left < rigth:

            while left < rigth and not s[left].isalnum():
                left += 1
            
            while left < rigth and not s[rigth].isalnum():
                rigth -= 1

            if s[left] != s[rigth]:
                return False

            left += 1
            rigth -= 1

        return True

