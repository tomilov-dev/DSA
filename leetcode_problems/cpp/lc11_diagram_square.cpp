#include <vector>
#include <iostream>
#include <algorithm>
using std::vector, std::max, std::min;

class Solution
{
public:
    int run(vector<int> height)
    {
        int p1 = 0;
        int p2 = height.size() - 1;
        int max_w = 0;

        int hgt;
        int wgt;

        while (p1 < p2)
        {
            int hgt = min(height[p1], height[p2]);
            int wgt = p2 - p1;

            max_w = max(max_w, (hgt * wgt));
            if (height[p1] < height[p2])
            {
                p1++;
            }
            else
            {
                p2--;
            }
        }

        return max_w;
    }
};

int main()
{
    vector<int> height = {1,
                          8,
                          6,
                          2,
                          5,
                          4,
                          8,
                          3,
                          7};

    Solution sol;

    int answer = sol.run(height);

    std::cout << answer << std::endl;
}