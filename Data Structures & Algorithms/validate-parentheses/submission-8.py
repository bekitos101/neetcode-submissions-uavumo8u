class Solution:
    def isValid(self, s: str) -> bool:
      #Brute force solution 
      #continiously remove valid brackets until no more can be removed 
      #TC O(n2) because of string operation/replacement
      while s: 
        old=s
        s=s.replace("()","")
        s=s.replace("[]","")
        s=s.replace("{}","")

        #After each iteration, if the strings didnt change , no valid pair remains
        #Since it's non empty, the brackets are invalid 
        if s==old:
            return False 
      #String became empty, all brackets were matched        
      return True

      #optimized solution
      #iterate through the string by index 
      #for an opening bracket push it onto the stack 
      #for a closing bracket check if the top of the stack corresponds to its 
      #opening bracket, if it's not found immediately, return false 


      hash_stk={"]":"[","}":"{",")":"("}  
      stk=[]
      for char in s:
        if char=="(" or char=="[" or char=="{":
            stk.append(char)
        
        if char=="]" or char==")" or char=="}":
            #stk is empty->nothing to match 
            if not stk:
                return False 
            if stk.pop()!=hash_stk[char]:
                return False 
        
        #valid only when no unmatched opening brackets remain 

        return len(stk)==0






    
