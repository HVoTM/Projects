from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        else:
            # if there is a node (root node, specifically)
            # height is now 1
            # we recursively call on the children nodes until no more nodes are present
            # return and add from the bottom up

            left_depth = self.maxDepth(root.left)
            right_depth = self.maxDepth(root.right)

            if left_depth > right_depth:
                return left_depth + 1
            else:
                return right_depth + 1