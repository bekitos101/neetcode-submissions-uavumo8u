class Solution:
    def isValid(self, s: str) -> bool:
      while s: 
        old=s
        s=s.replace("()","")
        s=s.replace("[]","")
        s=s.replace("{}","")
      

        if s==old:
            return False 
      return True
    
