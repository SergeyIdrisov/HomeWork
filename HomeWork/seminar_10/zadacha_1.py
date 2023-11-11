class Heap:
    class Node:
        def __init__(self, value, left=None, right=None):
            self.left = left
            self.right = right
            self.value = value

        def __repr__(self):
            value_list = self.listing()
            depth = 0
            counter = 0
            floor = []
            print(value_list)
            for i in range(len(value_list)):
                counter += 1
                if value_list[i]:
                    floor.append(value_list[i])
                else:
                    floor.append(None)

                if 2 ** depth == counter:
                    counter %= (2 ** depth)
                    depth += 1
                    print(*floor)
                    floor = []
                    continue

            return ''

        def listing(self) -> list:
            nodes_list = []

            if self.left:
                nodes_list.append(self.left)
            if self.right:
                nodes_list.append(self.right)
            for node in nodes_list:
                if not node:
                    continue
                if node.left:
                    nodes_list.append(node.left)
                else:
                    nodes_list.append(None)
                if node.right:
                    nodes_list.append(node.right)
                else:
                    nodes_list.append(None)
            value_list = [self.value]
            for node in nodes_list:
                if node:
                    value_list.append(node.value)
                else:
                    value_list.append(None)

            return value_list

        def get_value(self):
            return self.value

        def get_child(self, side='left'):
            if side == 'left':
                return self.left
            elif side == 'right':
                return self.right
            else:
                return ValueError

        def set_child(self, node, side='left'):
            if side == 'left':
                self.left = node
                return
            elif side == 'right':
                self.right = node
                return
            else:
                return ValueError

    def __init__(self):
        self.root = None
    def get_root(self):
        return self.root
    def add(self, num):
        assert isinstance(num, int)
        node = self.Node(num)
        if not self.root:
            self.root = node
            return
        current_node = self.root
        up_node = None
        while node.value > current_node.value:
            if not current_node.left:
                current_node.left = node
                return
            elif not current_node.right:
                current_node.right = node
                return
            up_node = current_node
            current_node = current_node.left
        if up_node:
            up_node.left = node
        node.left = current_node.left
        current_node.left = None
        node.right = current_node
        return

    def pop(self) -> int: # НАПИСАТЬ УДАЛЕНИЕ КОРНЯ
        min = self.value
        return 0

    def heapsort(self, N)-> list: # НАПИСАТЬ УДАЛЕНИЕ КОРНЯ N раз (построенная пирамида выводит упорядоченный список)

        return 0


heap = Heap()
heap.add(1)
heap.add(2)
heap.add(3)
heap.add(4)
heap.add(5)
heap.add(6)
heap.add(7)
heap.add(8)
heap.add(9)
heap.add(10)
heap.add(11)
print(heap.root)