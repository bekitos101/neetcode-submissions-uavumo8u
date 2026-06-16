class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def isAnagram(s:str,t:str):
            return sorted(s)==sorted(t) 

        result=list()
        seen=set()

        for i in range(len(strs)):
            if i in seen :
                continue 
            group=[strs[i]]
            seen.add(i)
            for j in range(i+1,len(strs)):
                if j in seen:
                    continue
                elif isAnagram(strs[i],strs[j]):
                    group.append(strs[j])
                    seen.add(j)
            result.append(group)
        return result

    #dry run 
    #i=0 strs=["act","pots","tops","cat","stop","hat"] group=["act"] seen=("act")
    #      j=1  strs[j]="pots"  
    #      j=2  strs[j]="tops"
    #      j=3  strs[j]="cat" isAnargam("act","cat")=true group=["act","cat"] seen=("act","cat") 
    #      j=4  strs[j]="stop"
    #      j=5  strs[j]="hat" => result=[["act","cat"]]
    #i=1 strs=["act","pots","tops","cat","stop","hat"] group=["pots"] seen=("act","cat","pots")
    #      j=2  strs[j]="tops"  isAnagram=True group=["pots","tops"] seen=("act","cat","pots","tops")
    #      j=3  strs[j]="cat" => continue 
    #      j=4  strs[j]="stop" => isAnagram=True group=["pots","tops","stop"] seen=("act","cat","pots","tops","stop")
    #      j=5   strs[j]="hat" => result=[["act","cat"],group=["pots","tops","stop"]]
    # i=2 strs[i]="tops" => it shouldnt be added to a group!

    #  code runs but fails at testcase strs=["",""] because storing values in seen will make us skip duplicates 
    #  however two duplicate strings make an anagram => solution is to store indices instead of values in seen 
    #  we can not check the same index more than once, however different indices can have duplicate values 
    




        