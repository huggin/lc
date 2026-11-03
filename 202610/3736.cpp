class Solution {
public:
  int minMoves(vector<int> &nums) {
    int ma = *max_element(nums.begin(), nums.end());
    int ans = 0;
    for (int num : nums) {
      ans += ma - num;
    }
    return ans;
  }
};
