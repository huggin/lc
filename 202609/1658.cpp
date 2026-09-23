class Solution {
public:
  int minOperations(vector<int> &nums, int x) {
    int curr = 0;
    unordered_map<int, int> m;
    m[0] = 0;
    for (int i = 0; i < nums.size(); ++i) {
      curr += nums[i];
      if (curr <= x)
        m[curr] = i + 1;
      else
        break;
    }
    int ans = nums.size() + 1;
    if (m.find(x) != m.end()) {
      ans = m[x];
    }
    curr = 0;
    for (int i = nums.size() - 1; i >= 0; --i) {
      curr += nums[i];
      if (m.find(x - curr) != m.end()) {
        ans = min(ans, (int)nums.size() - i + m[x - curr]);
      }
    }
    if (ans > nums.size())
      return -1;
    return ans;
  }
};
