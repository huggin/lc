class Solution {
public:
  int minMoves2(vector<int> &nums) {
    sort(nums.begin(), nums.end());
    int mid = nums.size() / 2;
    return transform_reduce(nums.begin(), nums.end(), 0, std::plus<>{},
                            [&](int a) { return abs(a - nums[mid]); });
  }
};
