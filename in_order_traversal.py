# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [root]
        final_arr = []
        if root is None:
            return final_arr

        while root.left is not None:
            stack.append(root.left)
            root = root.left
        while len(stack) > 0:
            node = stack.pop()

            if node.right is not None and hasattr(node.right, 'visited') == False:
                stack.append(node.right)
                node.right.visited = True
            if node.left is not None and hasattr(node.left, 'visited') == False:
                stack.append(node)
                stack.append(node.left)
            if node.left is None:
                final_arr.append(node.val)
                node.visited = True
            if node.left is not None and hasattr(node.left, 'visited') == True:
                final_arr.append(node.val)
                node.visited = True
        return final_arr

