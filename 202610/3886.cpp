class Solution {
  vector<int> nums;
  vector<int> sorted;

  bool f(int k) {
    for (int i = 0; i < nums.size(); i += k) {
      if (!g(i, i + k))
        return false;
    }
    return true;
  }

  bool g(int i, int j) {
    int idx = -1;
    bool bigger = false;
    for (int k = i; k < j; ++k) {
      if (nums[k] < sorted[i] || nums[k] > sorted[j - 1]) {
        return false;
      }
      if (nums[k] > sorted[i]) {
        bigger = true;
      } else if (nums[k] == sorted[i]) {
        idx = k;
        if (bigger) {
          break;
        }
      }
    }
    if (idx == -1)
      return false;
    int k = i;
    while (k < j && nums[idx] == sorted[k]) {
      ++idx;
      if (idx == j)
        idx = i;
      ++k;
    }
    return k == j;
  }

public:
  int sortableIntegers(vector<int> &nums) {
    int n = nums.size();
    vector<int> div;
    for (int i = 1; i <= n; ++i) {
      if (n % i == 0) {
        div.push_back(i);
      }
    }
    if (is_sorted(begin(nums), end(nums))) {
      return reduce(begin(div), end(div), 0);
    }
    this->nums = nums;
    sorted = nums;
    sort(begin(sorted), end(sorted));

    int ans = 0;
    for (int k : div) {
      if (f(k))
        ans += k;
    }
    return ans;
  }
};
