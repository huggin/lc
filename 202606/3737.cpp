class Solution {
public:
  int countMajoritySubarrays(vector<int> &nums, int target) {
    int n = nums.size();
    vector<int> ps(n + 1);
    for (int i = 0; i < n; ++i) {
      ps[i + 1] = ps[i] + (nums[i] == target);
    }
    int ans = 0;
    for (int i = 0; i < n; ++i) {
      for (int j = i; j < n; ++j) {
        int m = j - i + 1;
        if ((ps[j + 1] - ps[i]) * 2 > m) {
          ++ans;
        }
      }
    }
    return ans;
  }
};
