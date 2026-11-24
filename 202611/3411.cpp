class Solution {
public:
  int maxLength(vector<int> &nums) {
    int ans = 0;
    int n = nums.size();
    for (int i = 0; i < n; ++i) {
      for (int j = i + 1; j < n; ++j) {
        long long l = nums[i];
        long long g = nums[i];
        long long p = nums[i];
        bool ok = true;
        for (int k = i + 1; k <= j; ++k) {
          l = gcd(l, nums[k]);
          g = lcm(g, nums[k]);
          p *= nums[k];
          if (l * g < p) {
            ok = false;
            break;
          }
        }
        if (!ok)
          continue;
        if (l * g == p) {
          ans = max(ans, j - i + 1);
        }
      }
    }
    return ans;
  }
};
