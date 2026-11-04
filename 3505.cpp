class Solution {
public:
  long long minOperations(vector<int> &nums, int x, int k) {
    int n = nums.size();
    multiset<int> left, right;
    long long lv = 0, rv = 0;
    for (int i = 0; i < x; ++i) {
      right.insert(nums[i]);
      rv += nums[i];
    }
    int sl = x / 2;
    int sr = x - sl;
    while (left.size() < sl) {
      auto it = right.begin();
      lv += *it;
      left.insert(*it);
      rv -= *it;
      right.erase(it);
    }
    vector<long long> cnt(n - x + 1);
    int mid = *right.begin();
    cnt[0] = 1LL * mid * sl - lv + rv - 1LL * mid * sr;

    for (int i = 1; i < n - x + 1; ++i) {
      if (nums[i - 1] < *right.begin()) {
        lv -= nums[i - 1];
        left.erase(left.find(nums[i - 1]));
      } else {
        rv -= nums[i - 1];
        right.erase(right.find(nums[i - 1]));
      }
      rv += nums[i + x - 1];
      right.insert(nums[i + x - 1]);
      if (right.size() > sr) {
        auto it = right.begin();
        lv += *it;
        left.insert(*it);
        rv -= *it;
        right.erase(it);
      }
      if (*right.begin() < *left.rbegin()) {
        rv += *left.rbegin();
        lv -= *left.rbegin();
        rv -= *right.begin();
        lv += *right.begin();
        right.insert(*left.rbegin());
        left.erase(left.find(*left.rbegin()));
        left.insert(*right.begin());
        right.erase(right.begin());
      }
      mid = *right.begin();
      cnt[i] = 1LL * mid * sl - lv + rv - 1LL * mid * sr;
    }

    const long long oo = 1e15;
    vector<long long> dp(n - x + 1, oo);
    vector<long long> dp2(n - x + 1, oo);
    dp[0] = cnt[0];
    for (int i = 1; i < n - x + 1; ++i) {
      dp[i] = min(dp[i - 1], cnt[i]);
    }

    for (int j = 1; j < k; ++j) {
      fill(dp2.begin(), dp2.end(), oo);
      for (int i = 0; i < n - x + 1; ++i) {
        if (i > 0) {
          dp2[i] = dp2[i - 1];
        }
        if (i - x >= 0) {
          dp2[i] = min(dp2[i], dp[i - x] + cnt[i]);
        }
      }
      dp2.swap(dp);
    }
    return dp[n - x];
  }
};
