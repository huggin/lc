class Solution {
public:
  bool asteroidsDestroyed(int mass, vector<int> &asteroids) {
    sort(begin(asteroids), end(asteroids));
    long long tt = mass;
    for (int a : asteroids) {
      if (tt < a)
        return false;
      tt += a;
    }
    return true;
  }
};
