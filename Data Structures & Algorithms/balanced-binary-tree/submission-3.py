# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #brute force solution 
        # def height(node):
        #     if not node:
        #         return 0 
        #     return 1+ max(height(node.left),height(node.right))
        
        # if not root:
        #     return True
        # if abs (height(root.left)-height(root.right))> 1:
        #     return False 
        
        # return self.isBalanced(root.left) and self.isBalanced(root.right)
        
        #optimized solution => we need the height not not be recalculated at each step 
        # when we are at a node , we can know the height of the node using dfs 

        self.difference=0
        def dfs(node):
            if not node:
                return 0
            
            right=dfs(node.right)
            if right==-1:
                return -1
            left=dfs(node.left)
            if left==-1:
                return -1 
            self.difference=max(self.difference,abs(right-left))
            if self.difference>1:
                return -1 
            return 1+max(right,left)
        
        if not root:
            return True
        
        return dfs(root)!=-1
        
        # this solution is good we calculate the max difference and update at each step in the dfs and we return the height
        # but we are traversing the whole tree either weather it's unbalanced or not 
        # we can stop early by adding a simple condition on left and right 


        
        