# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def recu(node: TreeNode, depth: int):
            if(node.left == None and node.right == None):
                return depth
            elif(node.left == None):
                return (recu(node.right, depth + 1))
            elif(node.right == None):
                return recu(node.left, depth + 1)
            else:
                return max(recu(node.left, depth + 1), recu(node.right, depth + 1))
    
        if (root == None):
            return 0
        return recu(root, 1)

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if(root == None):
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return 1 + max(left, right)

