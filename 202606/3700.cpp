class Solution {
  using ll = long long;
  using Matrix = vector<vector<ll>>;
  static constexpr ll MOD = 1'000'000'007;

  Matrix MatMul(const Matrix &a, const Matrix &b) {
    int m = a.size();
    int n = a[0].size();
    int p = b[0].size();

    Matrix c(m, std::vector<ll>(p, 0));

    for (int i = 0; i < m; ++i) {
      for (int k = 0; k < n; ++k) {
        for (int j = 0; j < p; ++j) {
          c[i][j] = (c[i][j] + a[i][k] * b[k][j]) % MOD;
        }
      }
    }

    return c;
  }

  Matrix exp(Matrix a, int b) {
    int n = a.size();
    Matrix ans(n, vector<ll>(n));
    for (int i = 0; i < n; ++i) {
      ans[i][i] = 1;
    }
    while (b) {
      if (b & 1) {
        ans = MatMul(ans, a);
      }
      a = MatMul(a, a);
      b >>= 1;
    }
    return ans;
  }

  void debug(const Matrix &a) {
    int m = a.size();
    for (int i = 0; i < m; ++i) {
      for (int j = 0; j < m; ++j) {
        cout << a[i][j] << ' ';
      }
      cout << '\n';
    }
  }

public:
  int zigZagArrays(int n, int l, int r) {
    int m = r - l + 1;
    Matrix L(m, vector<ll>(m)), U(m, vector<ll>(m)), init(m, vector<ll>(m, 1));
    for (int i = 0; i < m; ++i) {
      for (int j = 0; j < m; ++j) {
        L[i][j] = i > j;
        U[i][j] = i < j;
      }
    }

    auto UL = MatMul(U, L);
    auto M = exp(UL, (n - 1) >> 1);
    if (!(n & 1)) {
      M = MatMul(L, M);
    }

    auto V = MatMul(init, M);
    ll ans = reduce(begin(V[0]), end(V[0])) % MOD;
    return ans * 2 % MOD;
  }
};
