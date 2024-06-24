# Definition for a binary tree node.
from math import inf
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def insertLevelOrder(self, arr: List[int],root: Optional['TreeNode'], i: int) -> Optional['TreeNode']:
        if(i < len(arr) and arr[i] != None):
            temp = TreeNode(arr[i])
            root = temp
            root.left = self.insertLevelOrder(arr, root.left, 2*i + 1)
            root.right = self.insertLevelOrder(arr, root.right, 2*(i+1))
        return root
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def recu(root: TreeNode, currMax: int):
            if(root == None):
                return 0
            if(root.val >= currMax):
                left = 1 + recu(root.left, root.val )
                right = recu(root.right, root.val)
            else:
                left = recu(root.left, currMax )
                right = recu( root.right, currMax)
            
            return left + right
        return recu(root, float(-inf))

sol = Solution()

arr = [3,1,4,3,None,1,5]
node = TreeNode()
node = node.insertLevelOrder(arr, node, 0)


print(sol.goodNodes(node))