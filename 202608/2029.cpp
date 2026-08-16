class Solution {
public:
  bool stoneGameIX(vector<int> &stones) {
    array<int, 3> cnt;
    for (int stone : stones) {
      ++cnt[stone % 3];
    }
    cnt[0] %= 2;
    auto f = [](int start, array<int, 3> c) -> bool {
      int need = start;
      bool flag = false;
      int curr = 0;
      while (c[need] > 0) {
        --c[need];
        curr = (curr + need) % 3;
        need = curr;
        if (c[0] == 1) {
          c[0] = 0;
          flag = true;
        } else if (c[need] > 0) {
          --c[need];
          curr = (curr + need) % 3;
        } else {
          if (c[1] == 0 && c[2] == 0)
            return false;
          return true;
        }
        need = curr;
      }
      return false;
    };
    return f(1, cnt) || f(2, cnt);
  }
};
