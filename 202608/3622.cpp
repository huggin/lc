class Solution {
public:
  bool checkDivisibility(int n) {
    string s = to_string(n);
    long long a = 0;
    long long b = 1;
    for (int i = 0; i < s.size(); ++i) {
      a += s[i] - '0';
      b *= s[i] - '0';
    }
    cout << a << ' ' << b << endl;
    return n % (a + b) == 0;
  }
};
