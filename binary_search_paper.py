import collections
import binary_search_tree as bst


class Paper:
    def __init__(self, bs_tree):
        """
        Init the list for transform the binary search tree into a list
        :param Tree() bs_tree: the tree (binary_search_tree.Tree()) to transform
        """
        self._tree = bs_tree

        self.area = [0]

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
                self.area.append(None)

            else:
                node = self._tree.search_node(val, True)[1]

                queue.append(node.l_subtree.value) if node.l_subtree else queue.append(None)
                queue.append(node.r_subtree.value) if node.r_subtree else queue.append(None)

                self.area.append(val)  # 10 6 16 1 8 20
                self.area[0] += 1

        for _ in range(sum([2**i for i in range(self._tree.height()+2)]) - (len(self.area)-1)):
            self.area.append(None)

    def insert(self, value, parent, l_subtree_value=None, r_subtree_value=None):
        pass

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

        while incr < len(self.area) and self.area[incr] != value:
            incr += 1

        return (not incr == len(self.area), incr) if return_index else not incr == len(self.area)

    def is_leaf(self, value):
        parent = self.search(value, True)[1]

        return self.area[2*parent] is None and self.area[(2*parent)+1] is None


if __name__ == '__main__':
    tree = bst.Tree(bst.Node(10))

    for v in [16, 6, 8, 20, 1]:
        tree.insert_node(bst.Node(v))

    paper = Paper(tree)
    paper.press_tree()

    print(paper.area)

    print(paper.is_leaf(10))
