class SegTree {
  vector<int> arr;
  vector<int> tree;
  int n;

public:
  SegTree(const vector<int> &arr) : arr(arr) {
    n = arr.size();
    tree.resize(4 * n);
    build(1, 0, n - 1);
  }

  void build(int i, int l, int r) {
    if (l == r) {
      tree[i] = arr[l];
      return;
    }
    int m = (l + r) >> 1;
    build(i << 1, l, m);
    build(i << 1 | 1, m + 1, r);
    tree[i] = max(tree[i << 1], tree[(i << 1) | 1]);
  }

  int query(int v, int tl, int tr, int l, int r) {
    if (l > r)
      return 0;
    if (tl == l && tr == r)
      return tree[v];
    int tm = tl + tr >> 1;
    return max(query(v << 1, tl, tm, l, min(r, tm)),
               query(v << 1 | 1, tm + 1, tr, max(l, tm + 1), r));
  }

  int query(int l, int r) { return query(1, 0, n - 1, l, r); }
};

class Solution {
public:
  vector<int> maxActiveSectionsAfterTrade(string s,
                                          vector<vector<int>> &queries) {
    int n = s.size();
    int cnt1 = count(begin(s), end(s), '1');
    vector<int> zb, bl, br;
    int i = 0;
    while (i < n) {
      int j = i;
      while (i < n && s[i] == s[j]) {
        ++i;
      }
      if (s[j] == '0') {
        zb.push_back(i - j);
        bl.push_back(j);
        br.push_back(i - 1);
      }
    }

    int m = zb.size();
    vector<int> ans(queries.size(), cnt1);
    if (m < 2)
      return ans;
    vector<int> a(m - 1);
    for (int i = 0; i < m - 1; ++i) {
      a[i] = zb[i] + zb[i + 1];
    }

    SegTree seg(a);
    for (const auto &[k, q] : std::views::enumerate(queries)) {
      int l = q[0], r = q[1];
      int i = lower_bound(begin(br), end(br), l) - begin(br);
      int j = upper_bound(begin(bl), end(bl), r) - begin(bl) - 1;
      if (i > m - 1 || j < 0 || i >= j) {
        continue;
      }
      int first = br[i] - max(bl[i], l) + 1;
      int last = min(br[j], r) - bl[j] + 1;
      if (i + 1 == j) {
        ans[k] += first + last;
        continue;
      }
      int v1 = first + zb[i + 1];
      int v2 = zb[j - 1] + last;
      int v3 = seg.query(i + 1, j - 2);
      ans[k] += max({v1, v2, v3});
    }
    return ans;
  }
};
