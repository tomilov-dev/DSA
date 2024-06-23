#include <vector>
#include <iostream>
#include <algorithm>

class Soltuion
{
public:
    int run(std::vector<int> &gain)
    {
        int highest = 0;
        int prev = highest;

        for (int num : gain)
        {
            int cur = prev + num;
            highest = std::max(highest, cur);
            prev = cur;
        }

        return highest;
    }
};

int main()
{
    std::vector<int> gain = {-5, 1, 5, 0, -7};

    Soltuion sol;
    int answer = sol.run(gain);

    std::cout << answer << std::endl;
    return 0;
}