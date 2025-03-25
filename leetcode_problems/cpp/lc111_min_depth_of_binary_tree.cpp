#include <algorithm>
#include <limits>

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
    int minDepthRec(TreeNode *node)
    {
        if (node == nullptr)
        {
            return std::numeric_limits<int>::max();
        }
        if (node->left == nullptr && node->right == nullptr)
        {
            return 1;
        }
        int left = minDepthRec(node->left);
        int right = minDepthRec(node->right);
        return std::min(left, right) + 1;
    }

    int minDepth(TreeNode *root)
    {
        if (root == nullptr)
        {
            return 0;
        }
        return minDepthRec(root);
    }
};
