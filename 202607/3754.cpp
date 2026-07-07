class Solution {
public:
  long long sumAndMultiply(int n) {
    string s = to_string(n);
    long long ans = 0;
    int sum = 0;
    for (char c : s) {
      if (c != '0') {
        int d = c - '0';
        ans = ans * 10 + d;
        sum += d;
      }
    }
    return ans * sum;
  }
};
