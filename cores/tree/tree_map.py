from typing import List


class TreeNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None


class TreeMap:
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        # recursive
        self.root = self._insert_helper(self.root, key, val)

        # # iterative
        # node = TreeNode(key, val)
        # if self.root == None:
        #     self.root = node
        #     return

        # curr = self.root
        # while curr:
        #     if key > curr.key:
        #         if not curr.right:
        #             curr.right = node
        #             return
        #         curr = curr.right
        #     elif key < curr.key:
        #         if not curr.left:
        #             curr.left = node
        #             return
        #         curr = curr.left
        #     else:
        #         curr.val = val
        #         return

    def _insert_helper(self, root: TreeNode, key: int, val: int) -> None:
        if not root:
            return TreeNode(key, val)

        if key > root.key:
            root.right = self._insert_helper(root.right, key, val)
        elif key < root.key:
            root.left = self._insert_helper(root.left, key, val)
        return root

    def get(self, key: int) -> int:
        curr: TreeNode = self.root
        while curr:
            if key > curr.key:
                curr = curr.right
            elif key < curr.key:
                curr = curr.left
            else:
                return curr.val
        return -1

    def getMin(self) -> int:
        curr = self.root
        while curr and curr.left:
            curr = curr.left
        return curr.val if curr else -1

    def getMax(self) -> int:
        curr = self.root
        while curr and curr.right:
            curr = curr.right
        return curr.val if curr else -1

    def findMin(self, node: TreeNode) -> TreeNode:
        while node and node.left:
            node = node.left
        return node

    def remove(self, key: int) -> None:
        self.root = self._remove_helper(self.root, key)

    def _remove_helper(self, curr: TreeNode, key: int):
        if not curr:
            return

        if key > curr.key:
            curr.right = self._remove_helper(curr.right, key)
        elif key < curr.key:
            curr.left = self._remove_helper(curr.left, key)
        else:
            if not curr.left:
                return curr.right
            elif not curr.right:
                return curr.left
            else:
                # min_node = self.findMin(curr.right)
                min_node = curr.right
                while min_node and min_node.left:
                    min_node = min_node.left
                curr.key = min_node.key
                curr.val = min_node.val
                curr.right = self._remove_helper(curr.right, min_node.key)
        return curr

    def getInorderKeys(self) -> List[int]:
        # recursive
        result = []
        self._inorder_traversal(self.root, result)
        return result

        # # iterative
        # stack = []
        # res = []
        # curr: TreeNode = self.root
        # while curr or stack:
        #     if curr:
        #         stack.append(curr)
        #         curr = curr.left
        #     else:
        #         curr = stack.pop()
        #         res.append(curr.key)
        #         curr = curr.right
        # return res

    def _inorder_traversal(self, root: TreeNode, result) -> List[int]:
        if root:
            self._inorder_traversal(root.left, result)
            result.append(root.key)
            self._inorder_traversal(root.right, result)


if __name__ == "__main__":
    tree_map = TreeMap()
    tree_map.insert(1, 2)
    tree_map.insert(4, 2)
    tree_map.insert(3, 7)
    tree_map.insert(2, 1)
    print(tree_map.getInorderKeys())

    print(tree_map.get(3))
    print(tree_map.getMin())
    print(tree_map.getMax())

    tree_map.remove(1)
    print(tree_map.getInorderKeys())
