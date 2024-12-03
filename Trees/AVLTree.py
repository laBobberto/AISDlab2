import random
from Trees.Node import Node
from Trees.Node import drawNodes



class AVLTree:
    def __init__(self):
        self.root = None

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
            result.append(current.key)
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
            result.append(node.key)
            self._inorder(node.right, result)
        return result

    def preorder(self):
        return self._preorder(self.root, [])

    def _preorder(self, node, result):
        if node:
            result.append(node.key)
            self._preorder(node.left, result)
            self._preorder(node.right, result)
        return result

    def postorder(self):
        return self._postorder(self.root, [])

    def _postorder(self, node, result):
        if node:
            self._postorder(node.left, result)
            self._postorder(node.right, result)
            result.append(node.key)
        return result

    def getBalanceFactor(self, node):
        if node is None:
            return 0
        return self._getHeight(node.left) - self._getHeight(node.right)

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):

        if node is None:
            return Node(key)

        if key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)


        node.height = 1 + max(self._getHeight(node.left), self._getHeight(node.right))


        balance = self.getBalanceFactor(node)




        if balance > 1 and key < node.left.key:
            return self.rightRotate(node)


        if balance < -1 and key > node.right.key:
            return self.leftRotate(node)


        if balance > 1 and key > node.left.key:
            node.left = self.leftRotate(node.left)
            return self.rightRotate(node)


        if balance < -1 and key < node.right.key:
            node.right = self.rightRotate(node.right)
            return self.leftRotate(node)

        return node

    def bestInsert(self, keys):
        sort_keys = sorted(keys)
        self.root = self._bestInsert(sort_keys)

    def _bestInsert(self, keys):
        if not keys:
            return None
        mid = len(keys) // 2
        root = Node(keys[mid])
        root.left = self._bestInsert(keys[:mid])
        root.right = self._bestInsert(keys[mid+1:])
        return root

    def averageInsert(self, keys):
        random.shuffle(keys)
        for value in keys:
            self.insert(value)

    def worstInsert(self, keys):
        keys = sorted(keys)
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
        self.root = self._delete(self.root, key)

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

            node.key = self._minValueNode(node.right).key
            node.right = self._delete(node.right, node.key)

        node.height = 1 + max(self._getHeight(node.left), self._getHeight(node.right))

        balance = self.getBalanceFactor(node)

        if balance > 1 and self.getBalanceFactor(node.left) >= 0:
            return self.rightRotate(node)


        if balance < -1 and self.getBalanceFactor(node.right) <= 0:
            return self.leftRotate(node)


        if balance > 1 and self.getBalanceFactor(node.left) < 0:
            node.left = self.leftRotate(node.left)
            return self.rightRotate(node)


        if balance < -1 and self.getBalanceFactor(node.right) > 0:
            node.right = self.rightRotate(node.right)
            return self.leftRotate(node)

        return node

    def rightRotate(self, y):
        x = y.left
        T2 = x.right


        x.right = y
        y.left = T2


        y.getHeight = max(self._getHeight(y.left), self._getHeight(y.right)) + 1
        x.getHeight = max(self._getHeight(x.left), self._getHeight(x.right)) + 1


        return x

    def leftRotate(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        x.getHeight = max(self._getHeight(x.left), self._getHeight(x.right)) + 1
        y.getHeight = max(self._getHeight(y.left), self._getHeight(y.right)) + 1

        return y

    def _minValueNode(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current


