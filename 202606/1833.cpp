class Solution {
public:
  int maxIceCream(vector<int> &costs, int coins) {
    sort(begin(costs), end(costs));
    int ans = 0;
    for (int i = 0; i < costs.size(); ++i) {
      if (coins >= costs[i]) {
        ++ans;
        coins -= costs[i];
      }
    }
    return ans;
  }
};
