class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #optimal solution:
        
        freq_hash={}
        for word in strs:
            signature="".join(sorted(word))
            if signature not in freq_hash:
                freq_hash[signature]=[]
            freq_hash[signature].append(word)
        return list(freq_hash.values())
            