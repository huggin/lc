def sort(a, lo, hi):
    if hi <= lo:
        return
    lt, gt = lo, hi
    v = a[lo]
    i = lo
    while i <= gt:
        if a[i] < v:
            a[lt], a[i] = a[i], a[lt]
            lt += 1
            i += 1
        elif a[i] > v:
            a[i], a[gt] = a[gt], a[i]
            gt -= 1
        else:
            i += 1
        
    sort(a, lo, lt - 1)
    sort(a, gt + 1, hi)

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        random.shuffle(nums)
        sort(nums, 0, len(nums)-1)
        return nums
