# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        ref = TreeNode()
        holder = ref

        def preorder(root):
            nonlocal ref
            if not root:
                return
    
            templ = root.left
            tempr = root.right
            
            ref.right = root 
            root.left = None
            ref = ref.right
            
            preorder(templ)
            preorder(tempr)

        preorder(root)
        root = holder.right
        