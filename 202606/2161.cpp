class Solution {
public:
  vector<int> pivotArray(vector<int> &nums, int pivot) {
    auto i = stable_partition(begin(nums), end(nums),
                              [=](int x) { return x < pivot; });
    stable_partition(i, end(nums), [=](int x) { return x == pivot; });
    return nums;
  }
};
