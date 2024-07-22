class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        a = []
        for i in range(len(names)):
            a.append((names[i], heights[i]))
        a.sort(key=lambda x: -x[1])
        return [c[0] for c in a]
