# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def searchBST(root: TreeNode, val: int):
    if not root:
        return None
    elif root.val == val:
        return root.val
    elif val > root.val:
        return searchBST(root.right, val)
    else:
        return searchBST(root.left, val)


root = TreeNode(4, 2, 7)
root.left = TreeNode(2, 1, 3)

print(searchBST(root, 2))