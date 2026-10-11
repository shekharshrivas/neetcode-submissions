# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # result = [float("-inf")]
        # def pathsum(root):
        #     if not root:
        #         return 0
        #     left = max(0, pathsum(root.left))
        #     right = max(0, pathsum(root.right))
        #     result[0] = max(result[0], left+right+root.val)
        #     return max(left, right) + root.val
        # pathsum(root)
        # return result[0]

        result = [float("-inf")]
        def pathsum(root):
            if not root:
                return 0
            left = max(0, pathsum(root.left))
            right = max(0, pathsum(root.right))
            result[0] = max(result[0], left + right + root.val)
            return root.val + max(left, right)
        pathsum(root)
        return result[0]
        