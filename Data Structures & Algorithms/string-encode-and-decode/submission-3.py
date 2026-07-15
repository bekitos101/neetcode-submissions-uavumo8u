class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded_string=""
        for s in strs:
            encoded_string+=str(len(s))+ "#"+s 
        return encoded_string  

    
    #example:
    #Input: strs = ["Hello","World"]
    # encoded_string=4#Hello4#World




    def decode(self,s:str)-> List[str]:
        decoded_string=[]
        i=0
        while i<len(s):
            delimiter_pos_end=s.find("#",i)
            length_word=int(s[i:delimiter_pos_end])
            word=s[delimiter_pos_end+1:delimiter_pos_end+1+length_word]
            decoded_string.append(word)
            i=delimiter_pos_end+1+length_word
        return decoded_string





    

        

        
        



        
