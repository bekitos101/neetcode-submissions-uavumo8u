class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #s = "XYYX", 
        # count={"x":2,"y":2}
        #k=2
        # replace x with 2ys or y with 2xs
        # max_length=4


        #s="AAABABB"
        # count={"A":4,"B":3}
        #k=1 
        # replace with the most frequent character in the string 
        # max_length=5 

        # brute force approach 
        # we have to maximize the length of the substring where we can have the most identical characters
        # in order to do that we need to count the frequency of the characters in that string 
        # since we are only allowed up to k permutations what we can do is: 
        # length of substring= count of the most frequent characters+ k permutations to the most frequent characters
        # O(n2) time complexity 
        max_substring=0 
        for i in range(len(s)):
            count={}
            for j in range(i,len(s)):
                count[s[j]]=count.get(s[j],0)+1
                most_frequent_char_count=max(count.values())
                if j-i+1-most_frequent_char_count<=k: # core idea 
                    max_substring=max(max_substring,j-i+1)
        return max_substring

        #optimized version: sliding window algorithm 
        left=0
        max_substring=0
        for right in range(len(s)):
            count={}
            most_frequent_char_count=max(count.values)
            if right-left+1-most_frequent_char_count>=k:
                count[s[left]]-=1
                left+=1
            count[s[right]]=count.get(s[right],0)+1
            max_substring=max(max_substring,j-i+1)
        return max_substring





        


        