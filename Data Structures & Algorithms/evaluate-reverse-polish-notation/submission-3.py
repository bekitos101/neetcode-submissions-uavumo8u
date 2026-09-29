class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        def calculate(left,right,op):
            res=0
            if op=="+":
                res=left+right
            elif op=="-":
                res=left-right
        
            elif op=="*":
                res=left*right
            else:
                res=int(left/right)
            return res 
        #brute force solution: actively find an operator and compute the result 
        # while len(tokens)>1:
        #     for i in range(len(tokens)):
        #         if tokens[i] in "+-*/":
        #             left=int(tokens[i-2])
        #             right=int(tokens[i-1])
        #             op=tokens[i]
        #             res=calculate(left,right,op)
        #             tokens[i-2:i+1]=[str(res)]
        #             break
            
        # return int(tokens[0])


        #Dry Run 
        #i=2 tokens[i]=+ left=1 right=2 op=+ tokens=["3","3","*","4","-"] break
        #i=2 tokens[i]=* left=3 right=3 op=* tokens=["9","4","-"] break 
        #i=2 tokens[i]=- left=9 right=4 op=- tokens=[5] break
        #no more iterations on token -> add condition to stop the infinite loop -> len(tokens)>1 
        

        #optimized solution: use a stack to keep track of the values before the operator , then store their result again in the stack 

        stk=[]
        for i in range(len(tokens)):
            if tokens[i] in "+-*/":
                right=stk.pop()
                left=stk.pop()
                op=tokens[i]
                res=calculate(int(left),int(right),op)
                stk.append(str(res))
            else:
                stk.append(tokens[i])
        
        return int(stk[-1])
            
        
        
        