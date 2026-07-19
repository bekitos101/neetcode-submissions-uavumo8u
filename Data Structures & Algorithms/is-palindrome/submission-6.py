class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        clean_string=""
        s.strip()
        for c in s:
            if c.isalnum():
                clean_string+=c.lower()
        print(clean_string[::-1])
        return clean_string[::-1]==clean_string