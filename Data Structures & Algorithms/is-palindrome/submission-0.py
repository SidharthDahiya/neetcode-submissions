class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = s.lower()
        s_Straight = []
        s_Reverse = []

        for i in range (0, len(s)):
            if not s[i].isalnum():
                continue
            s_Straight.append(s[i])

        for i in range(len(s) -1 , -1, -1):
            if not s[i].isalnum():
                continue
            s_Reverse.append(s[i])

        return s_Reverse == s_Straight