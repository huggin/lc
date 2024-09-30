class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = [0] * maxSize
        self.cap = maxSize
        self.pos = 0

    def push(self, x: int) -> None:
        if self.pos < self.cap:
            self.stack[self.pos] = x
            self.pos += 1

    def pop(self) -> int:
        if self.pos != 0:
            self.pos -= 1
            return self.stack[self.pos]
        return -1

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, self.pos)):
            self.stack[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
