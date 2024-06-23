#include <vector>
#include <iostream>
#include <algorithm>
using std::vector, std::min;

class Solution
{
public:
    int run(vector<int> &height)
    {
        if (height.size() <= 1)
        {
            return 0;
        }

        int N = height.size();
        int trapped = 0;
        int p1 = 0;
        int p2 = 1;

        while (height[p1] <= 0)
        {
            p1++;
            p2++;
        }
        while (height[N - 1] <= 0)
        {
            N--;
        }

        int local_max = p2; // pointer 2

        while (p1 < N && p2 < N) // (p2 < N - 1)
        {
            while (p2 < N && height[p1] > height[p2])
            {
                p2++;
                if (p2 < N && height[local_max] < height[p2])
                {
                    local_max = p2;
                }
            }

            int H = min(height[p1], height[local_max]);

            while (p1 < local_max)
            {
                if (height[p1] < H)
                {
                    trapped += (H - height[p1]);
                }
                p1++;
            }

            local_max++;
            p2 = local_max;
        }

        return trapped;
    }

    int run2(vector<int> &height)
    {
        const int N = height.size();
        int trapped = 0;
        int p1 = 0;
        int p2 = N - 1;

        int max_left = 0;
        int max_right = 0;

        while (p1 <= p2)
        {
            if (height[p1] <= height[p2])
            {
                if (height[p1] >= max_left)
                {
                    max_left = height[p1];
                }
                else
                {
                    trapped += max_left - height[p1];
                }
                p1++;
            }
            else
            {
                if (height[p2] >= max_right)
                {
                    max_right = height[p2];
                }
                else
                {
                    trapped += max_right - height[p2];
                }
                p2--;
            }
        }

        return trapped;
    }
};

int main()
{
    // vector<int> height = {4, 2, 0, 3, 2, 5}; // 9
    // vector<int> height = {7, 0, 0, 4, 4, 0, 3}; // 11
    // vector<int> height = {4, 2, 0, 3, 2, 5, 1, 3, 2, 0}; // 11
    vector<int> height = {0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1}; // 6
    // vector<int> height = {0, 0, 3, 4, 3, 2, 0, 4, 7, 9, 4, 0, 0, 3}; // 13

    Solution sol;
    auto answer = sol.run2(height);

    std::cout << answer << std::endl;
}