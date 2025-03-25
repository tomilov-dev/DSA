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
    TreeNode *build(vector<int> &nums, int start, int end)
    {
        if (start > end)
        {
            return nullptr;
        }

        int mid = start + (end - start) / 2;
        TreeNode *node = new TreeNode(nums[mid]);
        node->left = build(nums, start, mid - 1);
        node->right = build(nums, mid + 1, end);
        return node;
    }

    TreeNode *sortedArrayToBST(vector<int> &nums)
    {
        int n = nums.size();
        return build(nums, 0, n - 1);
    }
};
