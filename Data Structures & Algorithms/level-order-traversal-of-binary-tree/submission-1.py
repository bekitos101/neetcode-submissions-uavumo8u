# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque 
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res=[]
        q=deque()
        q.append(root)
        
        #dry run 
        #root = [1,2,3,4,5,6,7]
        # level=[] and level_size=1 q=[1]  i=0  node=1  q=[2,3] level=[1] res=[[1]] => done 
        # level=[] and level_size=2 q=[2,3] i=0 node=2 q=[3,4,5] level=[2] 
        #                                   i=1 node=3 q=[4,5,6,7] level=[2,3] res=[[1],[2,3]] => done 
        # level=[] and level_size=4 q=q=[4,5,6,7] i=0 node=4 level=[4] 
        #                                         i=1 node=3 level=[4,5]
        #                                         i=2 node=6 level=[4,5,6]
        #                                         i=3 node=7 level=[4,5,6,7] => res=[[1],[2,3],[4,5,6,7]]=> done 

        #At the start of each iteration, the queue contains exactly the nodes of the current level
        # the main idea is the len(q) is the the size of the level at each time 
        # because everytime we pop a root we add its children to the queue when they are discovered 
        # since bfs is a level traversal, this ensures that the len(q) after each pop corresponds to the number of children in the next level 

        while q: 
            level=[]
            level_size=len(q)
            # now the key idea is that each time we pop , we explore that level 
            for _ in range(level_size):
                node=q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)  
            res.append(level)
        return res