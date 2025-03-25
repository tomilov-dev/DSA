struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    int depth(TreeNode *node, int d) {
        if (node == nullptr) {
            return d;
        } else {
            int left = depth(node->left, d+1);
            int right = depth(node->right, d+1);
            if (left > right) {
                return left;
            } else {
                return right;
            }
        }
    }

    int maxDepth(TreeNode* root) {
        return depth(root, 0);
    }
};