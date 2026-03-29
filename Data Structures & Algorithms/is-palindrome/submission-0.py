class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.strip()
        stripped_char=""
        for char in s:
            if char.isalnum():
                stripped_char+=char.lower()
        print( stripped_char)
        print(stripped_char[::-1])
        return  stripped_char== stripped_char[::-1]

        