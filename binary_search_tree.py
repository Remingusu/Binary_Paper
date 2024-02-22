class Node:
    def __init__(self, value, l_subtree=None, r_subtree=None):
        self.value, self.l_subtree, self.r_subtree = value, l_subtree, r_subtree

    def __str__(self):
        return f"({self.l_subtree} - {self.value} - {self.r_subtree})"
        # return f"  -> {self.l_subtree}\n"\
        #        f"{self.value}\n"\
        #        f"  -> {self.r_subtree}"


class Tree:
    def __init__(self, root):
        """
        Create the tree with the given root
        :param root: Node()
        """
        self.root = root
        self.current_node = root

    def insert_node(self, node):
        """
        Add a node to the tree
        :param node: Node()
        :return: None
        """
        if self.current_node.value > node.value:
            if self.current_node.l_subtree is None:
                self.current_node.l_subtree = node
            else:
                self.current_node = self.current_node.l_subtree
                self.insert_node(node)

        else:
            if self.current_node.r_subtree is None:
                self.current_node.r_subtree = node
            else:
                self.current_node = self.current_node.r_subtree
                self.insert_node(node)

        self.current_node = self.root

    def delete_node(self):
        pass

    def search_node(self):
        pass

    def is_leaf(self, node):
        return self.root.l_subtree is None and self.root.r_subtree is None

    def __str__(self):
        return self.root.__str__()


class TraversingTree:
    def __init__(self):
        pass


if __name__ == '__main__':
    abr = Tree(Node(5))
    abr.insert_node(Node(3))
    abr.insert_node(Node(6))
    abr.insert_node(Node(2))
    abr.insert_node(Node(7))
    abr.insert_node(Node(4))
    print(abr)
