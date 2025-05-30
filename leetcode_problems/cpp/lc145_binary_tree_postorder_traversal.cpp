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
        traverse(node->right, res);
        res.push_back(node->val);
    }

    vector<int> postorderTraversal(TreeNode *root)
    {
        vector<int> res;
        traverse(root, res);
        return res;
    }
};
