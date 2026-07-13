class Solution {
  using ll = long long;

public:
  vector<int> sequentialDigits(int low, int high) {
    vector<int> ans;
    function<void(ll)> f = [&](ll curr) {
      if (curr > high)
        return;
      if (low <= curr && curr <= high) {
        ans.push_back(curr);
      }
      int last_digit = curr % 10;
      if (last_digit != 9) {
        ++last_digit;
        f(curr * 10 + last_digit);
      }
    };
    for (int i = 1; i < 10; ++i) {
      f(i);
    }
    sort(begin(ans), end(ans));
    return ans;
  }
};
