class Solution {
public:
  int smallestNumber(int n, int t) {
    auto f = [](int k) -> int {
      string s = to_string(k);
      return std::reduce(s.begin(), s.end(), 1,
                         [](int prod, char c) { return prod * (c - '0'); });
    };
    while (true) {
      if (f(n) % t == 0)
        return n;
      ++n;
    }
    return -1;
  }
};
