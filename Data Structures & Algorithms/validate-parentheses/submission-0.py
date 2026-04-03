class Solution:
    def isValid(self, s: str) -> bool:
        #s=""([{}])""
        
        #brute force idea: traverse this string 
        #check locally valid parentheses each time 

        while "()" in s or "[]" in s or "{}" in s:
            s=s.replace("{}","")
            s=s.replace("[]","")
            s=s.replace("()","")

        return s==""
