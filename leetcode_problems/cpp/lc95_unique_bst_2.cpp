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
    vector<TreeNode *> generate(int i, int n)
    {
        if (i > n)
        {
            return {nullptr};
        }

        vector<TreeNode *> nodes;
        for (int j = i; j <= n; j++)
        {
            vector<TreeNode *> lefts = generate(i, j - 1);
            vector<TreeNode *> rigths = generate(j + 1, n);
            for (TreeNode *left : lefts)
            {
                for (TreeNode *right : rigths)
                {
                    TreeNode *head = new TreeNode(j);
                    head->left = left;
                    head->right = right;
                    nodes.push_back(head);
                }
            }
        }
        return nodes;
    }

    vector<TreeNode *> generateTrees(int n)
    {
        return generate(1, n);
    }
};