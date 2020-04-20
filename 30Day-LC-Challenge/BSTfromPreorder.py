# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        inorder = sorted(preorder)
        return self.bstFromPreorderAndInorder(preorder, inorder)

    def bstFromPreorderAndInorder(self, preorder, inorder):
        lengthpre = len(preorder)
        lengthin = len(inorder)

        if lengthpre != lengthin or preorder == None or inorder == None or lengthpre == 0:
            return None
        root = TreeNode(preorder[0])
        rootindex = inorder.index(root.val)

        root.left = self.bstFromPreorderAndInorder(preorder[1:rootindex + 1], inorder[:rootindex])
        root.right = self.bstFromPreorderAndInorder(preorder[rootindex + 1:], inorder[rootindex + 1:])

        return root
