class Solution {
public:
  bool isRectangleOverlap(vector<int> &rec1, vector<int> &rec2) {
    auto f = [](int x1, int y1, int y2, int x2, int x3, int y3) {
      return x2 < x1 && x1 < x3 && y1 < y3 && y3 < y2;
    };
    auto include = [](int x1, int y1, int x2, int y2, int x3, int y3, int x4,
                      int y4) {
      return x1 <= x3 && y1 <= y3 && x2 >= x4 && y2 >= y4;
    };
    int x1 = rec1[0], y1 = rec1[1], x2 = rec1[2], y2 = rec1[3];
    int x3 = rec2[0], y3 = rec2[1], x4 = rec2[2], y4 = rec2[3];
    if (include(x1, y1, x2, y2, x3, y3, x4, y4) ||
        include(x3, y3, x4, y4, x1, y1, x2, y2))
      return true;
    return f(x1, y1, y2, x3, x4, y3) || f(x1, y1, y2, x3, x4, y4) ||
           f(x2, y1, y2, x3, x4, y3) || f(x2, y1, y2, x3, x4, y4) ||
           f(y1, x1, x2, y3, y4, x3) || f(y1, x1, x2, y3, y4, x4) ||
           f(y2, x1, x2, y3, y4, x3) || f(y2, x1, x2, y3, y4, x4);
  }
};
