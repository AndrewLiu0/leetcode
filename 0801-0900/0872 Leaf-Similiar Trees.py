# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def getLeafSeq(root: Optional[TreeNode]) -> []:
            q = deque()
            leafSeq = []
            q.append(root)
            while(len(q) > 0):
                curr = q.pop()
                if(curr.left == None and curr.right == None):
                    leafSeq.append(curr.val)
                if(curr.right != None):
                    q.append(curr.right)
                if(curr.left != None):
                    q.append(curr.left)
            return leafSeq
        leafSeq1 = getLeafSeq(root1)
        leafSeq2 = getLeafSeq(root2)
        if(len(leafSeq1) != len(leafSeq2)):
            return False
        for i in range(len(leafSeq1)):
            if(leafSeq1[i] != leafSeq2[i]):
                return False
        return True

            
