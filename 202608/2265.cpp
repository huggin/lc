/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left),
 * right(right) {}
 * };
 */
class Solution {
public:
  int averageOfSubtree(TreeNode *root) {
    int ans = 0;
    function<pair<int, int>(TreeNode * p)> f =
        [&](TreeNode *p) -> pair<int, int> {
      if (p == nullptr)
        return {0, 0};
      auto [l, lc] = f(p->left);
      auto [r, rc] = f(p->right);
      if ((l + r + p->val) / (lc + rc + 1) == p->val)
        ++ans;
      return {l + r + p->val, lc + rc + 1};
    };
    f(root);
    return ans;
  }
};
