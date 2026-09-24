class Solution {
public:
  int smallestIndex(vector<int> &nums) {
    for (auto [k, v] : std::views::enumerate(nums)) {
      int td = 0;
      while (v > 0) {
        td += v % 10;
        v /= 10;
      }
      if (td == k)
        return k;
    }
    return -1;
  }
};
