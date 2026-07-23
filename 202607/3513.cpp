class Solution {
public:
  int uniqueXorTriplets(vector<int> &nums) {
    if (nums.size() < 3)
      return nums.size();
    auto n = nums.size();
    if (!(n & (n - 1)))
      return n << 1;
    auto k = std::bit_width(n);
    return 1 << k;
  }
};
