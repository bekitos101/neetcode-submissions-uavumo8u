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
        def height(node):
            if not node:
                return 0
            return 1+ max(height(node.left),height(node.right))
            

        if not root:
            return 0
        current_diameter= height(root.left) + height(root.right) 

        left_diameter=self.diameterOfBinaryTree(root.left)
        right_diameter=self.diameterOfBinaryTree(root.right)

        return max(current_diameter,left_diameter,right_diameter)