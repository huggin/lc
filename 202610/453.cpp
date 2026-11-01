class Solution {
public:
  int minMoves(vector<int> &nums) {
    int mi = *min_element(nums.begin(), nums.end());
    int ret = accumulate(nums.begin(), nums.end(), -mi * nums.size());
    return ret;
  }
};
