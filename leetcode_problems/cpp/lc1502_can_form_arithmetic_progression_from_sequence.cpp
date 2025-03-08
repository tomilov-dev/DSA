#include <vector>
#include <algorithm>
#include <iostream>
using std::sort;
using std::vector;

class Solution
{
public:
    bool canMakeArithmeticProgression(vector<int> &arr)
    {
        sort(arr.begin(), arr.end());
        int diff = arr[1] - arr[0];
        for (int i = 2; i < arr.size(); i++)
        {
            if (arr[i] - arr[i - 1] != diff)
            {
                return false;
            }
        }
        return true;
    }
};

int main()
{
    vector<int> arr = {3, 5, 1};
    Solution sol;
    std::cout << sol.canMakeArithmeticProgression(arr) << std::endl;
    return 0;
}