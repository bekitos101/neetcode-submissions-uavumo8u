class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #Brute force solution
        #The only way to avoid duplicates is to add a set
        # we can not append lists to sets, they need to be converted to tuples
        #since we can compute the same sum many times in this impelementation if the numbers are redundent
        #we need to sort the triplet before adding it to the set
        #this solution is O(n3) time complexity (how many triplets we examin) and O(n2) space complexity(how many triplets we store => nums[i] is fixd, nums[j] is fixed => nums[k] forced )
        # result=[]
        # seen=set()
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         for k in range(j+1,len(nums)):
        #             triplet= [nums[i],nums[j],nums[k]]
        #             if sum(triplet)==0:
        #                 clean_triplet=tuple(sorted(triplet))
        #                 if clean_triplet not in seen:
        #                     seen.add(clean_triplet)
        #                     result.append(list(clean_triplet))                       
        # return result

        #optimized solution 
        #key idea a+b+c=target sum 
        # a is chosen ,b is chosen => c=-(a+b)=> so it's forced
        # the key idea is to sort the array => fix a , then the two pointer technique will solve for the two other numbers
        # duplicate handling: since the array is sorted we can check consecutive numbers, skip the index where they are identical 
        nums.sort()
        result=[]
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            left=i+1
            right=len(nums)-1
            while left<right:
                curr= nums[i]+nums[left]+nums[right]
                if curr==0:
                    triplet=[nums[i],nums[left],nums[right]]
                    result.append(triplet)
                    left+=1
                    right-=1

                    while left<right and nums[left]==nums[left-1]:
                        left+=1
                    while left<right and nums[right]==nums[right+1]:
                        right-=1
                elif curr <0:
                    left+=1
                elif curr>0:
                    right-=1
        return result
                    
                



     
                          