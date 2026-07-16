class Solution {
public:
  long long gcdSum(vector<int> &nums) {
    int mx = 0;
    vector<int> pre;
    for (int a : nums) {
      mx = max(mx, a);
      pre.push_back(gcd(a, mx));
    }
    sort(begin(pre), end(pre));
    int n = pre.size();
    long long ans = 0;
    for (int i = 0; i < n / 2; ++i) {
      ans += gcd(pre[i], pre[n - 1 - i]);
    }
    return ans;
  }
};
