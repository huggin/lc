class Solution {
public:
  int findGCD(vector<int> &nums) {
    auto [a, b] = std::minmax_element(begin(nums), end(nums));
    return std::gcd(*a, *b);
  }
};
