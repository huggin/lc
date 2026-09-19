class Solution {
public:
  bool checkOverlap(int radius, int xCenter, int yCenter, int x1, int y1,
                    int x2, int y2) {
    auto f = [=](int x, int y) -> bool {
      return (x - xCenter) * (x - xCenter) + (y - yCenter) * (y - yCenter) -
                 radius * radius <=
             0;
    };
    if (f(x1, y1) || f(x2, y2) || f(x1, y2) || f(x2, y1))
      return true;
    if (x1 < xCenter && xCenter < x2) {
      if (abs(y1 - yCenter) <= radius || abs(y2 - yCenter) <= radius)
        return true;
    }
    if (y1 < yCenter && yCenter < y2) {
      if (abs(x1 - xCenter) <= radius || abs(x2 - xCenter) <= radius)
        return true;
    }
    auto g = [=](int x, int y) -> bool {
      return x1 < x && x < x2 && y1 < y && y < y2;
    };
    if (g(xCenter, yCenter) || g(xCenter - radius, yCenter) ||
        g(xCenter + radius, yCenter) || g(xCenter, yCenter - radius) ||
        g(xCenter, yCenter + radius))
      return true;

    return false;
  }
};
