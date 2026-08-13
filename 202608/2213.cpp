struct Node {
  Node(int p = 0, int s = 0, int m = 0, int s2 = 1, char c1 = ' ',
       char c2 = ' ')
      : pre(p), suf(s), max(m), size(s2), first(c1), last(c2) {}
  int pre, suf, max, size;
  char first, last;
};

class SegTree {
  string s;
  vector<Node> tree;

public:
  SegTree(int n, const string &t) : s(t) {
    tree.resize(4 * n);
    build(1, 0, n - 1);
  }

  Node merge(const Node &l, const Node &r) {
    Node ans;
    ans.first = l.first;
    ans.last = r.last;
    ans.size = l.size + r.size;
    ans.max = max(l.max, r.max);
    if (l.last == r.first) {
      ans.max = max(ans.max, l.suf + r.pre);
    }
    ans.pre = l.pre;
    if (l.pre == l.size && l.last == r.first) {
      ans.pre = l.pre + r.pre;
    }
    ans.suf = r.suf;
    if (r.size == r.suf && l.last == r.first) {
      ans.suf = r.suf + l.suf;
    }
    return ans;
  }

  void build(int i, int l, int r) {
    if (l == r) {
      tree[i] = Node(1, 1, 1, 1, s[l], s[r]);
      return;
    }
    int m = (l + r) / 2;
    build(i * 2, l, m);
    build(i * 2 + 1, m + 1, r);
    tree[i] = merge(tree[2 * i], tree[2 * i + 1]);
  }

  Node query(int i, int l, int r, int tl, int tr) {
    if (l > r)
      return Node();
    if (l == tr && r == tr)
      return tree[i];
    int tm = (tl + tr) >> 1;
    Node left = query(i * 2, l, min(r, tm), tl, tm);
    Node right = query(i * 2 + 1, max(tm + 1, l), r, tm + 1, tr);
    Node ans = merge(left, right);
    return ans;
  }

  int query() { return tree[1].max; }

  void update(int i, int l, int r, int pos, char c) {
    if (l == r) {
      tree[i].first = tree[i].last = c;
      return;
    }
    int m = (l + r) >> 1;
    if (pos >= l && pos <= m) {
      update(i * 2, l, m, pos, c);
    } else {
      update(i * 2 + 1, m + 1, r, pos, c);
    }
    tree[i] = merge(tree[2 * i], tree[2 * i + 1]);
  }
};

class Solution {
public:
  vector<int> longestRepeating(string s, string queryCharacters,
                               vector<int> &queryIndices) {
    int n = queryIndices.size();
    vector<int> ans(n);
    SegTree sgt(s.size(), s);
    for (int i = 0; i < n; ++i) {
      sgt.update(1, 0, s.size() - 1, queryIndices[i], queryCharacters[i]);
      ans[i] = sgt.query();
    }
    return ans;
  }
};
