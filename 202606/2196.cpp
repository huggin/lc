/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* createBinaryTree(vector<vector<int>>& descriptions) {
        unordered_map<int, TreeNode*> nodes;
        for(const auto& des : descriptions) {
            TreeNode* child = nullptr;
            if (nodes.find(des[1]) == nodes.end()) {
                child = new TreeNode(des[1]);
                nodes[des[1]] = child;
            } else {
                child = nodes[des[1]];
            }
            TreeNode* parent = nullptr;
            if (nodes.find(des[0]) == nodes.end()) {
                parent = new TreeNode(des[0]);
                nodes[des[0]] = parent;
            } else {
                parent = nodes[des[0]];
            }
            if (des[2] == 0) {
                parent->right = child;
            } else {
                parent->left = child;
            }
        }
        for(const auto& des : descriptions) {
            nodes.erase(des[1]);
        }
        return nodes.begin()->second;
    }
};
