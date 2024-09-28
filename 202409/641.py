class Node:
    def __init__(self, val=-1):
        self.left = None
        self.right = None
        self.val = val


class MyCircularDeque:

    def __init__(self, k: int):
        self.cap = k
        self.head = None
        self.rear = None
        self.size = 0

    def insertFront(self, value: int) -> bool:
        if self.size == self.cap:
            return False
        if self.size == 0:
            self.head = self.rear = Node(value)
        else:
            p = Node(value)
            self.head.left = p
            p.right = self.head
            self.head = p
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.size == self.cap:
            return False
        if self.size == 0:
            self.head = self.rear = Node(value)
        else:
            p = Node(value)
            self.rear.right = p
            p.left = self.rear
            self.rear = p
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.head is None:
            return False
        self.head = self.head.right
        if self.head is None:
            self.rear = None
        else:
            self.head.left = None
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.rear is None:
            return False
        self.rear = self.rear.left
        if self.rear is None:
            self.head = None
        else:
            self.rear.right = None
        self.size -= 1
        return True

    def getFront(self) -> int:
        if self.head is None:
            return -1
        return self.head.val

    def getRear(self) -> int:
        if self.rear is None:
            return -1
        return self.rear.val

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.cap


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
