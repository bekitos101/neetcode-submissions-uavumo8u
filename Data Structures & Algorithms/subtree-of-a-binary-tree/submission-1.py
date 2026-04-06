# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSameSubtree(p,q):
            if not p and not q:
                return True 
            if not p or not q:
                return False 
            if p.val!=q.val:
                return False 
            
            return isSameSubtree(p.left,q.left) and isSameSubtree(p.right,q.right)


        def dfs(node):
            if not node:
                return False 
            
            # for the current root, subroot, check if we have the same tree
            if isSameSubtree(node,subRoot):
                return True 
            
            #otherwise check the subroot in the left or right node of the main tree 

            return dfs(node.left) or dfs(node.right)

        
        return dfs(root)


            