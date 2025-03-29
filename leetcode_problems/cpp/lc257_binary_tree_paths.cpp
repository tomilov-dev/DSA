#include <vector>
#include <string>
#include <functional>
using std::string;
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
    void backtrack(TreeNode *node, string &cur, vector<string> &res)
    {
        if (node == nullptr)
        {
            return;
        }

        if (!cur.empty())
        {
            cur += "->";
        }
        cur += std::to_string(node->val);

        if (node->left == nullptr && node->right == nullptr)
        {
            res.push_back(cur);
        }
        else
        {
            backtrack(node->left, cur, res);
            backtrack(node->right, cur, res);
        }

        int removeLength = std::to_string(node->val).size();
        if (!cur.empty() && cur.size() > removeLength)
        {
            removeLength += 2;
        }
        cur.erase(cur.size() - removeLength);
    }

    vector<string> binaryTreePaths(TreeNode *root)
    {
        vector<string> res;
        string cur;
        backtrack(root, cur, res);
        return res;
    }
};
