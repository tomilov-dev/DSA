#include <vector>
#include <iostream>
#include <expected>
using std::vector;

class Solution
{
public:
    int countGoodTriplets(vector<int> &arr, int a, int b, int c)
    {
        int count = 0;
        int n = arr.size();
        for (int i = 0; i < n; i++)
        {
            for (int j = i + 1; j < n; j++)
            {
                for (int k = j + 1; k < n; k++)
                {
                    if (std::abs(arr[i] - arr[j]) <= a && std::abs(arr[j] - arr[k]) <= b && std::abs(arr[i] - arr[k]) <= c)
                    {
                        count++;
                    }
                }
            }
        }
        return count;
    }
};

int main()
{
    std::vector<int> arr = {3, 0, 1, 1, 9, 7};
    int a = 7, b = 2, c = 3;

    Solution sol;
    int answer = sol.countGoodTriplets(arr, a, b, c);

    std::cout << "Answer is:" << answer << std::endl;
    return 0;
}