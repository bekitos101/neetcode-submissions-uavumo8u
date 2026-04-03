#brute force solution: all of the operations bellow are o(1)
#except for the last one it's o(n)
# we need to find a way to get min in o(1) time 


# class MinStack:

#     def __init__(self):
#         self.stack=[] 
        

#     def push(self, val: int) -> None:
#         self.stack.append(val)
        

#     def pop(self) -> None:
#         self.stack.pop()
        

#     def top(self) -> int:
#         return self.stack[-1]
        

#     def getMin(self) -> int:
#         return min(self.stack)

#input =[5,1,2,0,4]
#stack=[5,1,2,0,4]
# min_stack=[5,1,1,0,0]

class MinStack:

    def __init__(self):
        self.stk=[] 
        self.min_stk=[]
        
    # if stk=> if stack is not empty 
    #if not stk => if stack is empty 

    def push(self, val: int) -> None:
        self.stk.append(val)
        
        if self.min_stk and val>self.min_stk[-1]:
            self.min_stk.append(self.min_stk[-1])
        else:
            self.min_stk.append(val)

    def pop(self) -> None:
        self.stk.pop()
        self.min_stk.pop()
        

    def top(self) -> int:
        return self.stk[-1]
        

    def getMin(self) -> int:
        return self.min_stk[-1]

        
        
