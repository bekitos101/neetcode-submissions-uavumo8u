class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded_string=""
        for s in strs:
            encoded_string+=str(len(s))+ "#"+s 
        return encoded_string  




    def decode(self, s: str) -> List[str]:
        decoded_string=[]
        i=0
        while i<len(s):
            # this method finds the first occurance unless we specify 
            #the lookup start and end 
            delimiter_pos_end=s.find('#',i)
            string_length=int (s[i:delimiter_pos_end])
            decoded_string.append(s[delimiter_pos_end+1:delimiter_pos_end+1+string_length])
            i=delimiter_pos_end+1+string_length
        return decoded_string
      

        

        
        



        
