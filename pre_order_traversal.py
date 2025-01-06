# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        final_arr = []
        stack = [root]

        while stack:

            rootVal = stack.pop()

            if rootVal is not None:
                final_arr.append(rootVal.val)
                stack.append(rootVal.right)
                stack.append(rootVal.left)

        return final_arr