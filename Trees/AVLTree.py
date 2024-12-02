import random
from Node import Node
from Trees.Node import drawNodes


class AVLTree:
    def __init__(self):
        self.root = None

    def height(self):
        return self._height(self.root)

    def drawTree(self):
        drawNodes(self.root)


    def inorder(self):
        return self._inorder(self.root, [])

    def preorder(self):
        return self._preorder(self.root, [])

    def postorder(self):
        return self._postorder(self.root, [])

    def levelOrder(self):
        return self._levelOrder()

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def bestInsert(self, keys):
        sort_keys = sorted(keys)
        self.root = self._bestInsert(sort_keys)

    def averageInsert(self, keys):
        random.shuffle(keys)
        for value in keys:
            self.insert(value)

    def worstInsert(self, keys):
        for key in keys:
            self.insert(key)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def search(self, key):
        return self._search(self.root, key)

    def _bestInsert(self, keys):
        if not keys:
            return None
        mid = len(keys) // 2
        root = Node(keys[mid])
        root.left = self._bestInsert(keys[:mid])
        root.right = self._bestInsert(keys[mid+1:])
        return root

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.key)
            self._inorder(node.right, result)
        return result


    def _preorder(self, node, result):
        if node:
            result.append(node.key)
            self._preorder(node.left, result)
            self._preorder(node.right, result)
        return result

    def _postorder(self, node, result):
        if node:
            self._postorder(node.left, result)
            self._postorder(node.right, result)
            result.append(node.key)
        return result

    def _levelOrder(self):
        if not self.root:
            return []
        result = []
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            result.append(current.key)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return result



    def _insert(self, node, key):
        if node is None:
            return Node(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        else:
            return node  # Duplicate keys are not allowed

        node.height = 1 + max(self._height(node.left), self._height(node.right))

        return self._balance(node)


    def _delete(self, node, key):
        if not node:
            return node

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left

            temp = self._getMinNode(node.right)
            node.key = temp.key
            node.right = self._delete(node.right, temp.key)

        node.height = 1 + max(self._height(node.left), self._height(node.right))

        return self._balance(node)

    def _getMinNode(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def _height(self, node):
        if node is None:
            return 0
        left_height = self._height(node.left)
        right_height = self._height(node.right)
        return max(left_height, right_height) + 1


    def _search(self, node, key):
        if node is None:
            return False
        if key == node.key:
            return True
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

    def _balance(self, node):
        balance_factor = self._getBalance(node)

        if balance_factor > 1:
            if self._getBalance(node.left) < 0:
                node.left = self._rotateLeft(node.left)
            return self._rotateRight(node)

        if balance_factor < -1:
            if self._getBalance(node.right) > 0:
                node.right = self._rotateRight(node.right)
            return self._rotateLeft(node)

        return node

    def _getBalance(self, node):
        if not node:
            return 0
        return self._height(node.left) - self._height(node.right)

    def _rotateLeft(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self._height(z.left), self._height(z.right))
        y.height = 1 + max(self._height(y.left), self._height(y.right))

        return y

    def _rotateRight(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self._height(z.left), self._height(z.right))
        y.height = 1 + max(self._height(y.left), self._height(y.right))

        return y



