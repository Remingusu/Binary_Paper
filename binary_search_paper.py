import collections
import binary_search_tree as bst


class Paper:
    def __init__(self, bs_tree):
        """
        Init the list for transform the binary search tree into a list
        :param Tree() bs_tree: the tree (binary_search_tree.Tree()) to transform
        """
        self._tree = bs_tree

        self._area = [0]

    def press_tree(self):
        """
        Transform the binary search tree into list
        :return: None
        """
        queue = collections.deque()
        queue.append(self._tree.root.value)

        while len(queue) != 0:
            val = queue.popleft()

            if val is None:
                self._area.append(None)

            else:
                node = self._tree.search_node(val, True)[1]

                queue.append(node.l_subtree.value) if node.l_subtree else queue.append(None)
                queue.append(node.r_subtree.value) if node.r_subtree else queue.append(None)

                self._area.append(val)  # 10 6 16 1 8 20
                self._area[0] += 1

        for _ in range(sum([2 ** i for i in range(self._tree.height() + 2)]) - (len(self._area) - 1)):
            self._area.append(None)

    def insert(self, value, parent):
        """
        Insert a value in the list
        :param int value: the value to insert
        :param int parent: the parent of the value to insert
        :return: None
        """
        parent_index = self.search(parent, True)[1]

        if value > self._area[parent_index]:
            self._area[(2 * parent_index) + 1] = value

        else:
            self._area[2 * parent_index] = value

        for _ in range(2):
            self._area.append(None)

    def delete(self, value):
        pass

    def search(self, value, return_index=False):
        """
        Search for the value in the area
        :param int value: value to search
        :param bool return_index: return the index of the value if found
        :return bool | [bool, int]: False if not found, True otherwise. Return the index in addition if return_index
        """
        incr = 1

        while incr < len(self._area) and self._area[incr] != value:
            incr += 1

        return (not incr == len(self._area), incr) if return_index else not incr == len(self._area)

    def is_leaf(self, value):
        """
        Check if the value is a leaf
        :param int value: value to check if value is leaf
        :return bool: True if two None child, False otherwise
        """
        parent = self.search(value, True)[1]

        return self._area[2 * parent] is None and self._area[(2 * parent) + 1] is None

    def __str__(self):
        return str(self._area)


if __name__ == '__main__':
    tree = bst.Tree(bst.Node(10))

    for v in [16, 6, 8, 20, 1]:
        tree.insert_node(bst.Node(v))

    paper = Paper(tree)
    paper.press_tree()

    print(paper)

    # print("20 est une feuille:", paper.is_leaf(20))  # True
    # print("10 est une feuille:", paper.is_leaf(10))  # False

    # print("8 est présent:", paper.search(8))  # True
    # print("0 est présent:", paper.search(0))  # False

    # paper.insert(14, 16)
    # paper.insert(3, 1)

    # print(paper)
