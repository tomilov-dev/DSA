#include <vector>
#include <iostream>
using std::vector;

class Solution
{
public:
    vector<int> run(vector<int> &aster)
    {
        int backstep = aster.size() - 2;
        bool prev_sign = aster[backstep + 1] >= 0;
        while (backstep >= 0)
        {
            bool sign = aster[backstep] >= 0;
            if (prev_sign != sign)
            {
                if (abs(aster[backstep + 1]) == abs(aster[backstep]))
                {
                    aster.pop_back();
                    aster.pop_back();
                    backstep--;
                }
                else if (abs(aster[backstep + 1]) > abs(aster[backstep]))
                {
                    aster[backstep] = aster[backstep + 1];
                    aster.pop_back();
                }
                else
                {
                    aster.pop_back();
                    prev_sign = sign;
                }
            }
            backstep--;
        }

        return aster;
    }
};

int main()
{
    // vector<int> asteroids = {5, 10, -5};
    vector<int> asteroids = {8, -8};
    // vector<int> asteroids = {10, 2, -5};

    Solution sol;
    auto answer = sol.run(asteroids);

    for (auto ast : answer)
    {
        std::cout << ast << std::endl;
    }
}