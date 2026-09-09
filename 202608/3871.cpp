class Solution {
public:
  long long countCommas(long long n) {

    long long ans = 0;
    if (n < 1000)
      return 0;
    if (n < 1'000'000LL) {
      ans += (n - 999);
    } else if (n < 1'000'000'000LL) {
      ans += (999999 - 999);
      ans += (n - 999999) * 2;
    } else if (n < 1'000'000'000'000LL) {
      ans += (999999 - 999);
      ans += (999999999LL - 999999) * 2;
      ans += (n - 999999999) * 3;
    } else if (n < 1000000000000000LL) {
      ans += (999999 - 999);
      ans += (999999999 - 999999) * 2;
      ans += (999999999999LL - 999999999) * 3;
      ans += (n - 999999999999LL) * 4;
    } else {
      ans += (999999 - 999);
      ans += (999999999 - 999999) * 2;
      ans += (999999999999LL - 999999999) * 3;
      ans += (999999999999999LL - 999999999999LL) * 4;
      ans += 5;
    }
    return ans;
  }
};
