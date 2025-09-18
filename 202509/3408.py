class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.pq = []
        self.items = {}
        for task in tasks:
            entry = [-task[2], -task[1], task[0]]
            heapq.heappush(self.pq, entry)
            self.items[-task[1]] = entry.copy()

    def add(self, userId: int, taskId: int, priority: int) -> None:
        entry = [-priority, -taskId, userId]
        heapq.heappush(self.pq, entry)
        self.items[-taskId] = entry.copy()

    def edit(self, taskId: int, newPriority: int) -> None:
        old_priority, tid, uid = self.items[-taskId]
        self.items[-taskId] = [-newPriority, tid, uid]
        heapq.heappush(self.pq, [-newPriority, tid, uid])

    def rmv(self, taskId: int) -> None:
        old_priority, tid, uid = self.items[-taskId]
        self.items[-taskId] = [1, tid, uid]

    def execTop(self) -> int:
        while len(self.pq):
            pri, tid, uid = heapq.heappop(self.pq)
            if self.items[tid][0] != pri or self.items[tid][2] != uid:
                continue
            else:
                self.items[tid][0] = 1
                return uid
        return -1


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()
