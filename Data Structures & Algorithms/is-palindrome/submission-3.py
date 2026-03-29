class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s=s.strip()
        # stripped_char=""
        # for char in s:
        #     if char.isalnum():
        #         stripped_char+=char.lower()
        # print( stripped_char)
        # print(stripped_char[::-1])
        # return  stripped_char== stripped_char[::-1]

      
        #tabacat n=7
        #i=0, l-i=7 => ok 
        #i=1, l-i=6 => ok 
        #i=2 , l-i=5 => fail !

        # for i in range(0,l-1):
        #     print (i)
        #     if not s[i].isalnum():
        #         continue
        #     elif s[i]!=s[l-i-1]:
        #         return False 
        #     else:
        #         continue 
        # return True

        #tabacat n=7
        #left=0 right=6
        #left=1 right=5
        #left=2 right=4 

        s=s.strip()
        s=s.replace(" ","")
        s=s.lower()
        print(len(s))
        print(s)
        left=0
        right=len(s)-1
        while(left<right):
            if not s[left].isalnum():
               left+=1
               continue
            if not s[right].isalnum():
                right-=1
                continue 
            if s[left]!=s[right]:
                return False  
            else:
                left+=1
                right-=1
        return True 


        #dry run 
        #a.b,.
        #left=0  right=4 => nums[right]=. => right=3 
        #left=0  right=3=>  nums[right]=, => right=2 
        #left=0  right=2=>  nums[left]!=nums[right]=> False 
        