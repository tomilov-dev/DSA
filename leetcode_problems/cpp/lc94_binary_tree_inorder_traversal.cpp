#include <vector>
using std::vector;

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
    void traverse(TreeNode *node, vector<int> &res)
    {
        if (node == nullptr)
        {
            return;
        }

        traverse(node->left, res);
        res.push_back(node->val);
        traverse(node->right, res);
    }

    vector<int> inorderTraversal(TreeNode *root)
    {
        vector<int> res;
        traverse(root, res);
        return res;
    }
};
