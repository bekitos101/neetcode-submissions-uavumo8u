# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:        
        # At any node, the longest path through that node is: left height + right height 
        # we keep the maximum so we keep 1 + max (left height, right height)            
        #so first we write the height function 
        # we know that at each node , the diameter is height(left) + height(right) 
        #
        # def height(node):
        #     if not node:
        #         return 0
        #     return 1+ max(height(node.left),height(node.right))
            

        # if not root:
        #     return 0
        # current_diameter= height(root.left) + height(root.right) 

        # left_diameter=self.diameterOfBinaryTree(root.left)
        # right_diameter=diameterOfBinaryTree(root.right)

        # return max(current_diameter,left_diameter,right_diameter)

        
        #optimized solution 
        # can I avoid computing the height everytime we travel to a new node ?
        # right now we compute heights => then compute diameter
        # can we compute both at the same time ? =>yes with dfs 
        self.diameter=0 
        #gets the height at each step + computes diameter 
        def dfs(node):
            if not node:
                return 0
            left=dfs(node.left)
            right=dfs(node.right)
            self.diameter=max(self.diameter,left+right)
            return 1+ max(left,right)
        
        dfs(root)
        return self.diameter 
        
