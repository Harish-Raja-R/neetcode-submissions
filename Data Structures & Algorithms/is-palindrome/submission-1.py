class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2=""
        for i in range(0,len(s)):
            if s[i].isalnum():
                s2+=s[i].lower()
        return s2==s2[::-1]

                