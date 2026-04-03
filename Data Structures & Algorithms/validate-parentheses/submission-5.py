class Solution:
    def isValid(self, s: str) -> bool:
        #s=""([{}])""
        
        #Brute force idea: traverse this string 
        #Check locally valid parentheses each time 
        #Time complexity: O(n2) 


        # while "()" in s or "[]" in s or "{}" in s:
        #     s=s.replace("{}","")
        #     s=s.replace("[]","")
        #     s=s.replace("()","")

        # return s==""

        #optimized solution 
        # Optimized solution (stack-based)

        # Key observations:
        # 1. Each closing bracket must match the correct type of opening bracket
        # 2. Brackets must close in the correct order (LIFO: Last In, First Out)

        # optimized solution 
        # we have two things to ensure: correct type + correct closing order (LIFO)

        # use a hashmap to map each opening to its closing bracket 
        # when we see an opening bracket → push its expected closing into the stack 
        # this way we preserve both order and type 

        # when we see a closing bracket → check if it matches the top of the stack 
        # if yes → pop 
        # if not → invalid 

        # at the end, if the stack is empty → valid, else → invalid


        p_hash={"(":")","{":"}","[":"]"}
        stk=[]

        for char in s:
            #we have an opening bracket 
            if char in p_hash:
                closing_p=p_hash[char]
                stk.append(closing_p)
            #we have a closing bracket
            else:
                # stack is empty : no closing brackt=> flase + check if the top of the stack is not the closing bracket=> false  
                if not stk or char!=stk[-1]:
                    return False 
                stk.pop()
        return not stk 

        #stk=empty => not stk: returns true, stk:returns false 

