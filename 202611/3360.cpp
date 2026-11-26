class Solution {
public:
  bool canAliceWin(int n) {
    int round = 10;
    bool flag = false;
    while (n >= round) {
      n -= round;
      --round;
      flag = !flag;
    }
    return flag;
  }
};
