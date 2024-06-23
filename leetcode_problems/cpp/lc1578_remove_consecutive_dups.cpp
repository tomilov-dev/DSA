#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
using std::string, std::vector;

class Solution
{
public:
    int run(string colors, vector<int> &time)
    {
        int total = 0;
        int prev_index = 0;

        for (int index = 1; index < colors.length(); index++)
        {
            if (colors[prev_index] == colors[index])
            {
                int drop_index = time[prev_index] >= time[index] ? index : prev_index;
                total += time[drop_index];

                if (drop_index == prev_index)
                {
                    prev_index = index;
                }
            }
            else
            {
                prev_index = index;
            }
        }

        return total;
    }

    int run2(string colors, vector<int> &time)
    {
        int total = 0;
        for (int index = 1; index < colors.length(); index++)
        {
            if (colors[index] == colors[index - 1])
            {
                total += std::min(time[index], time[index - 1]);
                time[index] = std::max(time[index], time[index - 1]);
            }
        }
        return total;
    }
};

int main()
{
    string colors = "aabaa";
    vector<int> neededTime = {1, 2, 3, 4, 1};

    Solution sol;
    auto answer = sol.run(colors, neededTime);

    std::cout << answer << std::endl;
}