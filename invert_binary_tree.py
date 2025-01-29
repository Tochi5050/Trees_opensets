# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root

        return self.invertTreeHelper(root)

    def invertTreeHelper(self, root):
        if root is not None:
            root.left, root.right = root.right, root.left

            # if root.left is not None and root.right is not None:
            self.invertTreeHelper(root.left)
            self.invertTreeHelper(root.right)

        # if root.left is None or root.right is None:
        #     return root

        return root

