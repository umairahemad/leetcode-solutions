class Solution:
    def reverseVowels(self, s: str) -> str:
  

        vowels = {'a','A','e','E','i','I','o','O','u','U'}
        s = list(s)

        ### extract all vowels from s
        vowelInS = [c for c in s if c in vowels]

        ### replace the vowels in s with the reversed ones
        for i in range(len(s)):
            if s[i] in vowels:
                s[i] = vowelInS.pop(-1)

        return ''.join(s)