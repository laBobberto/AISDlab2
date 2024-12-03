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
        self.RED = "red"
        self.BLACK = "black"

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

    def _rotate_left(self, node):
        right = node.right
        node.right = right.left
        if right.left:
            right.left.parent = node
        right.parent = node.parent
        if not node.parent:
            self.root = right
        elif node == node.parent.left:
            node.parent.left = right
        else:
            node.parent.right = right
        right.left = node
        node.parent = right

    def _rotate_right(self, node):
        left = node.left
        node.left = left.right
        if left.right:
            left.right.parent = node
        left.parent = node.parent
        if not node.parent:
            self.root = left
        elif node == node.parent.right:
            node.parent.right = left
        else:
            node.parent.left = left
        left.right = node
        node.parent = left

    def _fix_insert(self, node):
        while node.parent and node.parent.color == self.RED:
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle and uncle.color == self.RED:
                    node.parent.color = self.BLACK
                    uncle.color = self.BLACK
                    node.parent.parent.color = self.RED
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self._rotate_left(node)
                    node.parent.color = self.BLACK
                    node.parent.parent.color = self.RED
                    self._rotate_right(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle and uncle.color == self.RED:
                    node.parent.color = self.BLACK
                    uncle.color = self.BLACK
                    node.parent.parent.color = self.RED
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self._rotate_right(node)
                    node.parent.color = self.BLACK
                    node.parent.parent.color = self.RED
                    self._rotate_left(node.parent.parent)
        self.root.color = self.BLACK

    def insert(self, key):
        new_node = Node(key, color=self.RED)
        parent = None
        current = self.root

        while current:
            parent = current
            if new_node.key < current.key:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent
        if not parent:
            self.root = new_node
        elif new_node.key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

        self._fix_insert(new_node)

    def _transplant(self, u, v):
        if not u.parent:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v:
            v.parent = u.parent

    def _minimum(self, node):
        while node.left:
            node = node.left
        return node

    def _fix_delete(self, node):
        while node != self.root and node.color == self.BLACK:
            if node == node.parent.left:
                sibling = node.parent.right
                if sibling.color == self.RED:
                    sibling.color = self.BLACK
                    node.parent.color = self.RED
                    self._rotate_left(node.parent)
                    sibling = node.parent.right
                if (not sibling.left or sibling.left.color == self.BLACK) and \
                        (not sibling.right or sibling.right.color == self.BLACK):
                    sibling.color = self.RED
                    node = node.parent
                else:
                    if not sibling.right or sibling.right.color == self.BLACK:
                        if sibling.left:
                            sibling.left.color = self.BLACK
                        sibling.color = self.RED
                        self._rotate_right(sibling)
                        sibling = node.parent.right
                    sibling.color = node.parent.color
                    node.parent.color = self.BLACK
                    if sibling.right:
                        sibling.right.color = self.BLACK
                    self._rotate_left(node.parent)
                    node = self.root
            else:
                sibling = node.parent.left
                if sibling.color == self.RED:
                    sibling.color = self.BLACK
                    node.parent.color = self.RED
                    self._rotate_right(node.parent)
                    sibling = node.parent.left
                if (not sibling.left or sibling.left.color == self.BLACK) and \
                        (not sibling.right or sibling.right.color == self.BLACK):
                    sibling.color = self.RED
                    node = node.parent
                else:
                    if not sibling.left or sibling.left.color == self.BLACK:
                        if sibling.right:
                            sibling.right.color = self.BLACK
                        sibling.color = self.RED
                        self._rotate_left(sibling)
                        sibling = node.parent.left
                    sibling.color = node.parent.color
                    node.parent.color = self.BLACK
                    if sibling.left:
                        sibling.left.color = self.BLACK
                    self._rotate_right(node.parent)
                    node = self.root
        node.color = self.BLACK

    def delete(self, key):
        node = self.root
        while node and node.key != key:
            if key < node.key:
                node = node.left
            else:
                node = node.right

        if not node:
            return

        original_color = node.color
        if not node.left:
            replacement = node.right
            self._transplant(node, node.right)
        elif not node.right:
            replacement = node.left
            self._transplant(node, node.left)
        else:
            successor = self._minimum(node.right)
            original_color = successor.color
            replacement = successor.right
            if successor.parent == node:
                if replacement:
                    replacement.parent = successor
            else:
                self._transplant(successor, successor.right)
                successor.right = node.right
                successor.right.parent = successor

            self._transplant(node, successor)
            successor.left = node.left
            successor.left.parent = successor
            successor.color = node.color

        if original_color == self.BLACK:
            self._fix_delete(replacement)

    def search(self, key):
        current = self.root
        while current:
            if key == current.key:
                return True
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        return False

    def averageInsert(self, keys):
        def insertion(keys):
            if not keys:
                return
            mid = len(keys) // 2
            self.insert(keys[mid])
            insertion(keys[:mid])
            insertion(keys[mid + 1:])

        keys = sorted(keys)
        insertion(keys)

    def bestInsert(self, keys):
        random_keys = keys[:]
        random.shuffle(random_keys)
        for key in random_keys:
            self.insert(key)

    def worstInsert(self, keys):
        keys = sorted(keys)
        for key in keys:
            self.insert(key)

