from typing import List, Optional

# from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.inorderTraversal(root, result)
        return result

    def inorder_traverse(self, node: Optional[TreeNode], result: List[int]):
        if node is None:
            return
        self.inorder_traverse(node.left, result)
        result.append(node.val)
        self.inorder_traverse(node.right, result)

        # result = []
        # if root is not None:
        #     return root
        # while root.left == True:
        #     return result.append(root)
        # return result


# check if tree exists
# if true check the value of first node
# append first node value to the result List
# check if value exists left of first node
# if true: append value of linked left node to the result list
# check if value exists on the following node (current node)
# if true: append value of linked linked node to the result list
