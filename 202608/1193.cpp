class Solution {
public:
  int maxNumberOfFamilies(int n, vector<vector<int>> &reservedSeats) {
    unordered_map<int, array<int, 11>> res;
    for (int i = 0; i < reservedSeats.size(); ++i) {
      res[reservedSeats[i][0]][reservedSeats[i][1]] = 1;
    }
    int ans = (n - res.size()) * 2;
    for (const auto &[_, v] : res) {
      int curr = 0;
      if (v[2] == 0 && v[3] == 0 && v[4] == 0 && v[5] == 0)
        ++curr;
      if (v[6] == 0 && v[7] == 0 && v[8] == 0 && v[9] == 0)
        ++curr;
      if (curr == 0 && v[6] == 0 && v[7] == 0 && v[4] == 0 && v[5] == 0)
        ++curr;
      ans += curr;
    }
    return ans;
  }
};
