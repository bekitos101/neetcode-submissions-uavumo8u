class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Brute force approach
        # For every possible substring, count the frequency of each character.
        # Keep the most frequent character -> this keeps the maximum number of characters unchanged
        # and therefore minimizes the number of replacements needed.
        # replacements = substring length - highest character frequency
        # k = maximum number of replacements we are allowed to make.
        # If replacements <= k, the substring is valid -> update the maximum length.

        # def get_count(substring):
        #     count={}
        #     for char in s:
        #         count[char]=count.get(char,0)+1
        #     return count
        # max_length=0
        # for i in range(len(s)):
        #     for j in range(i+1,len(s)):
        #         substring=s[i:j+1]
        #         count=get_count(substring)
        #         max_freq=max(count.values())
        #         replacements=(j-i+1)-max_freq
        #         if replacements<=k:
        #             max_length=max(max_length,j-i+1)
        # return max_length

        #optimized approach: sliding window 
        #expand window: keep the state of the string with each added character 
        #shrink window condition: replacements>=k
        #window valid again: calculate current max_substring 

        left=0
        count={}

        max_length=0 
        for right in range(len(s)):
            #expand window 
            count[s[right]]=count.get(s[right],0)+1
            replacements=(right-left+1)-max(count.values())

            #shrink winodw 
            while replacements>k:
                count[s[left]]-=1
                left+=1
                #update replacements
                replacements=(right-left+1)-max(count.values())

            #window valid again 
            max_length=max(max_length,right-left+1)
        return max_length



       