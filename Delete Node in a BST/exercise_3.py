# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if root is None:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            parent = root
            child = root.right

            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left


            while child.left is not None:
                parent = child
                child = child.left
            
            if parent != root:
                parent.left = child.right
            else:
                root.right = child.right

            root.val = child.val

        return root
