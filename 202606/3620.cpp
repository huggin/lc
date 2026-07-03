class Solution {
public:
  int findMaxPathScore(vector<vector<int>> &edges, vector<bool> &online,
                       long long k) {
    int n = online.size();
    vector<vector<pair<int, int>>> adj(n);
    for (const auto edge : edges) {
      if (online[edge[0]] && online[edge[1]]) {
        adj[edge[0]].emplace_back(edge[1], edge[2]);
      }
    }
    long long oo = 6e13;

    auto f = [&](int mv) -> bool {
      vector<long long> dist(n, oo);
            dist[…st[v]) {
        dist[v] = d + w;
        pq.emplace(dist[v], v);
                    }
    }
  }
  return dist[n - 1] <= k;
};

int lo = 0, hi = int(1e9);
int ans = -1;
while (lo <= hi) {
  int mi = lo + hi >> 1;
  if (f(mi)) {
    ans = mi;
    lo = mi + 1;
  } else {
    hi = mi - 1;
  }
}
return ans;
}
}
;
