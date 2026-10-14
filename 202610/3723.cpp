class Solution {
public:
  string maxSumOfSquares(int num, int sum) {
    if (num * 9 < sum)
      return "";
    string ans;
    while (ans.size() < num) {
      if (sum >= 9) {
        ans.push_back('9');
        sum -= 9;
      } else {
        ans.push_back('0' + sum);
        if (num > ans.size())
          ans += string(num - ans.size(), '0');
        break;
      }
    }
    return ans;
  }
};
