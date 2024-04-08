class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n = len(students)
        j = 0
        used = [0] * n
        for i in range(n):
            cnt = 0
            while cnt < n:
                if used[j] == 0 and students[j] == sandwiches[i]:
                    used[j] = 1
                    break
                j = (j + 1) % n
                cnt += 1

            if cnt == n:
                return n - i

        return 0
