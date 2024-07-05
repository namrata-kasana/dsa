class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right, s = 0, len(s) - 1, s.lower()
        while left < right:
            while (not self.isAlfaNumeric(s[left]) and left < right):
                left = left + 1
            while (not self.isAlfaNumeric(s[right]) and right > left):
                right = right - 1
            if s[right] != s[left]:
                return False
            left, right = left + 1, right - 1
        return True

    def isAlfaNumeric(self, s):
        return (ord('a') <= ord(s) <= ord('z') or ord('A') <= ord(s) <= ord('Z') or ord('0') <= ord(s) <= ord('9'))

testObj=Solution()
print(testObj.isPalindrome("racecar"))