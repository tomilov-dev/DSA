from utils import TreeNode


class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode | None:
        def build(inorder: list[int], postorder: list[int]) -> TreeNode | None:
            if len(inorder) == 0 or len(postorder) == 0:
                return None

            rootVal = postorder.pop()
            root = TreeNode(rootVal)
            inPos = inorder.index(rootVal)

            root.right = build(inorder[inPos + 1 :], postorder)
            root.left = build(inorder[:inPos], postorder)
            return root

        # Оптимизация с маппером не работает, т.к. мы режем массив
        # На каждом шаге рекурсии у нас меняются индексы массива
        return build(inorder, postorder)
