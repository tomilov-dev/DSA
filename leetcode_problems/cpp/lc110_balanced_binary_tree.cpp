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
private:
    bool balanced;
    int height(TreeNode *node)
    {
        if (node == nullptr)
        {
            return 0;
        }
        int left = height(node->left);
        int right = height(node->right);
        if (std::abs(left - right) > 1)
        {
            balanced = false;
        }
        return std::max(left, right) + 1;
    }

public:
    bool
    isBalanced(TreeNode *root)
    {
        balanced = true;
        height(root);
        return balanced;
    }
};
