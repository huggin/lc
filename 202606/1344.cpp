class Solution {
public:
  double angleClock(int hour, int minutes) {
    double a = minutes / 60.0 * 360;
    double b = hour % 12 * 30 + minutes / 60.0 * 30;
    double ans = abs(a - b);
    return min(ans, 360 - ans);
  }
};
