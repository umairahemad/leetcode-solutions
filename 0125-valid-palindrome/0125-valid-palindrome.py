class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""
        for character in s:
            if character.isalnum():
                cleaned += character.lower()
        return  cleaned == cleaned[::-1]