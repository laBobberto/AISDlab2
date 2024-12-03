import random
from Trees.Node import drawNodes

class Node:
    def __init__(self, key, color="red", left=None, right=None):
        self.left = left
        self.right = right
        self.key = key
        self.label = str(key)
        self.parent = None
        self.color = color


class RedBlackTree:
    def __init__(self):
        self.root = None

    RED = "red"
    BLACK = "black"

    def getHeight(self, node):
        if node is None:
            return 0
        left_height = self._getHeight(node.left)
        right_height = self._getHeight(node.right)
        return max(left_height, right_height) + 1

    def _getHeight(self, node):
        if node is None:
            return 0
        left_height = self._getHeight(node.left)
        right_height = self._getHeight(node.right)
        return max(left_height, right_height) + 1

    def drawTree(self):
        drawNodes(self.root)


    def levelorder(self):
        if not self.root:
            return []
        result = []
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            result.append([current.key, current.color])
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return result

    def inorder(self):
        return self._inorder(self.root, [])

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append([node.key, node.color])
            self._inorder(node.right, result)
        return result

    def preorder(self):
        return self._preorder(self.root, [])

    def _preorder(self, node, result):
        if node:
            result.append([node.key, node.color])
            self._preorder(node.left, result)
            self._preorder(node.right, result)
        return result

    def postorder(self):
        return self._postorder(self.root, [])

    def _postorder(self, node, result):
        if node:
            self._postorder(node.left, result)
            self._postorder(node.right, result)
            result.append([node.key, node.color])
        return result

    def insert(self, key):
        self.root = self._insert(self.root, key)
        self.root.color = self.BLACK

    def _insert(self, node, key):
        if node is None:
            return Node(key, self.RED)

        if key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)

        if self.isRed(node.right) and not self.isRed(node.left):
            node = self.leftRotate(node)

        if self.isRed(node.left) and self.isRed(node.left.left):
            node = self.rightRotate(node)

        if self.isRed(node.left) and self.isRed(node.right):
            self.flipColors(node)

        return node

    def leftRotate(self, node):
        x = node.right
        node.right = x.left
        x.left = node
        x.color = node.color
        node.color = self.RED
        return x

    def rightRotate(self, node):
        x = node.left
        node.left = x.right
        x.right = node
        x.color = node.color
        node.color = self.RED
        return x

    def flipColors(self, node):
        node.color = self.RED
        node.left.color = self.BLACK
        node.right.color = self.BLACK

    def isRed(self, node):
        return node is not None and node.color == self.RED

    def bestInsert(self, keys):
        sort_keys = sorted(keys)
        self.root = None
        self._bestInsert(sort_keys)

    def _bestInsert(self, keys):
        """
        Рекурсивно вставляет ключи из отсортированного списка, сохраняя свойства красно-черного дерева.
        """
        if not keys:
            return
        mid = len(keys) // 2
        self.insert(keys[mid])
        self._bestInsert(keys[:mid])
        self._bestInsert(keys[mid + 1:])

    def averageInsert(self, keys):
        random.shuffle(keys)
        for value in keys:
            self.insert(value)

    def worstInsert(self, keys):
        for key in keys:
            self.insert(key)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None:
            return False
        if key == node.key:
            return True
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

    def delete(self, key):
        if self.root is None:
            return None
        self.root = self._delete(self.root, key)
        if self.root:
            self.root.color = self.BLACK

    def _delete(self, node, key):
        if node is None:
            return node

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            min_node = self._minValueNode(node.right)
            node.key = min_node.key
            node.right = self._delete(node.right, min_node.key)

        return node

    def moveRedLeft(self, node):
        self.flipColors(node)
        if self.isRed(node.right.left):
            node.right = self.rightRotate(node.right)
            node = self.leftRotate(node)
            self.flipColors(node)
        return node

    def moveRedRight(self, node):
        self.flipColors(node)
        if self.isRed(node.left.left):
            node = self.rightRotate(node)
            self.flipColors(node)
        return node

    def balance(self, node):
        if self.isRed(node.right):
            node = self.leftRotate(node)
        if self.isRed(node.left) and self.isRed(node.left.left):
            node = self.rightRotate(node)
        if self.isRed(node.left) and self.isRed(node.right):
            self.flipColors(node)
        return node

    def fixAfterDelete(self, node):
        if self.isRed(node.right):
            node = self.leftRotate(node)
        if self.isRed(node.left) and self.isRed(node.left.left):
            node = self.rightRotate(node)
        if self.isRed(node.left) and self.isRed(node.right):
            self.flipColors(node)
        return node

    def balance(self, node):
        if self.isRed(node.right):
            node = self.leftRotate(node)
        if self.isRed(node.left) and self.isRed(node.left.left):
            node = self.rightRotate(node)
        if self.isRed(node.left) and self.isRed(node.right):
            self.flipColors(node)
        return node

    def _minValueNode(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
