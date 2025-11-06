from utils import TreeNode


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        def build(preorder: list[int], inorder: list[int]) -> TreeNode | None:
            if not preorder or not inorder:
                return None

            rootVal = preorder.pop(0)
            inPos = inorder.index(rootVal)
            root = TreeNode(rootVal)
            root.left = build(preorder, inorder[:inPos])
            root.right = build(preorder, inorder[inPos + 1 :])
            return root

        # Оптимизация с маппером не работает, т.к. мы режем массив
        # На каждом шаге рекурсии у нас меняются индексы массива
        return build(preorder, inorder)
