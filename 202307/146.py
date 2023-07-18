class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.size = 0
        self.dict = {}
        self.head = None
        self.tail = None

    def remove_node(self, node):
        if node == self.head:
            self.head = node.next
        else:
            node.prev.next = node.next

        if node == self.tail:
            self.tail = node.prev
        else:
            node.next.prev = node.prev

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        node = self.dict[key]
        self.remove_node(node)
        self.push_to_front(node)
        return node.val

    def push_to_front(self, node):
        node.next = self.head
        if self.head is not None:
            self.head.prev = node
        else:
            self.tail = node
        self.head = node

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            node = self.dict[key]
            node.val = value
            if node == self.head:
                return

            self.remove_node(node)
        else:
            self.size += 1
            if self.size > self.cap:
                del self.dict[self.tail.key]
                self.tail = self.tail.prev
                if self.tail is None:
                    self.head = None
                self.size -= 1

            node = Node(key, value)
            self.dict[key] = node
        self.push_to_front(node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
