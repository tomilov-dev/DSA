#include <algorithm>

struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution
{
public:
    bool countPathSum(TreeNode *node, int sum, int target)
    {
        if (node == nullptr)
        {
            return false;
        }
        sum += node->val;
        if (sum == target && node->left == nullptr && node->right == nullptr)
        {
            return true;
        }
        return countPathSum(node->left, sum, target) || countPathSum(node->right, sum, target);
    }

    bool hasPathSum(TreeNode *root, int targetSum)
    {
        if (root == nullptr)
        {
            return false;
        }
        return countPathSum(root, 0, targetSum);
    }
};
