import collections


class Node:
    def __init__(self, value, l_subtree=None, r_subtree=None, parent=None, side=0):
        self.value, self.l_subtree, self.r_subtree, self.parent, self.side = value, l_subtree, r_subtree, parent, side

    def __str__(self):
        return f"({self.l_subtree} - {self.value} - {self.r_subtree})"


class Tree:
    def __init__(self, root):
        """
        Generate a tree with the given root
        :param Node() root: the first node of the tree
        """
        self.root = root
        self.current_node = root

    def insert_node(self, node):
        """
        Add a node to the tree
        :param Node() node: the node to insert
        """
        if self.current_node.value > node.value:
            if self.current_node.l_subtree is None:
                node.parent = self.current_node
                node.side = 0
                self.current_node.l_subtree = node
            else:
                self.current_node = self.current_node.l_subtree
                self.insert_node(node)

        else:
            if self.current_node.r_subtree is None:
                node.side = 1
                node.parent = self.current_node
                self.current_node.r_subtree = node
            else:
                self.current_node = self.current_node.r_subtree
                self.insert_node(node)

        self.current_node = self.root

    def delete_node(self, node_value, leaf_deleting=False):
        """
        Delete a node from the tree
        :param int node_value: the value of the node to delete | The value need to be in the tree
        :param bool leaf_deleting: private value. if we want to delete a node who has two children
        """
        node = self.search_node(node_value, True)[1]
        node_side = node.side
        node_parent = node.parent

        # le nœud est une feuille
        if self.is_leaf(node_value, leaf_deleting):

            if node_side == 0:
                node_parent.l_subtree = None
            else:
                node_parent.r_subtree = None

        # le nœud a 2 enfants
        elif node.l_subtree is not None and node.r_subtree is not None:
            self.current_node = node

            next_node_value = self.current_node.r_subtree

            while next_node_value.l_subtree is not None:
                next_node_value = next_node_value.l_subtree

            self.current_node.value = next_node_value.value

            inf_value = float('-inf')
            next_node_value.value = inf_value

            self.current_node = self.current_node.r_subtree

            self.delete_node(inf_value, True)

        # le noeud a 1 enfant
        elif node.l_subtree or node.r_subtree:
            self.current_node = node

            node_child = node.l_subtree if node.l_subtree else node.r_subtree

            self.current_node.value = node_child.value
            inf_value = float('-inf') if node.l_subtree else float('inf')
            node_child.value = inf_value

            self.delete_node(inf_value, True)

        self.current_node = self.root

    def search_node(self, node_value, return_node=False):
        """
        Search the node in the tree
        :param int node_value: the value of the node to search
        :param bool return_node: return the node in addition if he's found, and if this param is True
        :return: False if not found, True otherwise
        """
        if self.current_node is None:
            self.current_node = self.root
            return False

        elif self.current_node.value == node_value:

            if return_node:
                node_package = (True, self.current_node)
                self.current_node = self.root
                return node_package

            return True

        elif self.current_node.value > node_value:
            self.current_node = self.current_node.l_subtree
            return self.search_node(node_value, return_node)

        elif self.current_node.value < node_value:
            self.current_node = self.current_node.r_subtree
            return self.search_node(node_value, return_node)

    def is_leaf(self, node_value, leaf_deleting=False):
        """
        Check if the node have subtrees (give value of the node)
        :param int node_value: the value of the node to check | Value need to be in the tree
        :param bool leaf_deleting: if we want to delete a node with 2 children (private)
        :return: False if not leaf, True otherwise
        """
        if leaf_deleting:
            return True
        node = self.search_node(node_value, True)[1]
        return node.l_subtree is None and node.r_subtree is None

    def __str__(self):
        return self.root.__str__()


class TraversingTree:
    def __init__(self, bst):
        self.root = bst.root

        self.preorder_list = []
        self.inorder_list = []
        self.postorder_list = []

        self.level_list = []

    def depth_traversal(self):
        def _wrapper(current_node):
            if current_node is None:
                return

            self.preorder_list.append(current_node.value)
            _wrapper(current_node.l_subtree)
            self.inorder_list.append(current_node.value)
            _wrapper(current_node.r_subtree)
            self.postorder_list.append(current_node.value)

        _wrapper(self.root)

    def level_traversal(self):
        queue = collections.deque()
        queue.append(self.root)

        while len(queue) != 0:
            node = queue.popleft()

            queue.append(node.l_subtree) if node.l_subtree else None
            queue.append(node.r_subtree) if node.r_subtree else None

            self.level_list.append(node.value)


if __name__ == '__main__':
    abr = Tree(Node(10))

    for val in [16, 6, 8, 20, 1]:
        abr.insert_node(Node(val))

    # tt = TraversingTree(abr)
    #
    # tt.level_traversal()
    # tt.depth_traversal()

    print(abr)

    # print("Level order of the BST", tt.level_list)
    # print("Pre-order of the BST:", tt.preorder_list)
    # print("In-order of the BST:", tt.inorder_list)
    # print("Post-order of the BST:", tt.postorder_list)
    #
    # print("16 present:", abr.search_node(16))  # True
    # print("21 present:", abr.search_node(21))  # False
    #
    # print("16 leaf:", abr.is_leaf(16))  # False
    # print("1 leaf:", abr.is_leaf(1))  # True
    #
    # abr.delete_node(1)
    # abr.delete_node(16)
    # abr.delete_node(10)
    # abr.delete_node(6)
    # print(abr)  # ((None - 8 - None) - 20 - None)
