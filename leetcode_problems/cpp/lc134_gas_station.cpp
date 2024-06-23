#include <vector>
#include <iostream>
using std::vector;

class Solution1
{
public:
    int trip(vector<int> &gas,
             vector<int> &cost,
             int start_index,
             int N)
    {
        int gas_amount = 0;
        int step = start_index;
        step = step == N ? 0 : step;

        while (true)
        {
            gas_amount += gas[step];
            gas_amount -= cost[step];
            if (gas_amount < 0)
            {
                break;
            }

            step++;
            step = step == N ? 0 : step;

            if (step == start_index)
            {
                return true;
            }
        }

        return false;
    }

    int run(vector<int> &gas, vector<int> &cost)
    {
        int N = gas.size();
        for (int start_index = 0; start_index < N; start_index++)
        {
            if (trip(gas, cost, start_index, N))
            {
                return start_index;
            }
        }

        return -1;
    }
};

class Solution2
{
public:
    int run(vector<int> &gas, vector<int> &cost)
    {
        int N = gas.size();
        int total_surplus = 0;
        int surplus = 0;
        int start_index = 0;

        for (int step = 0; step < N; step++)
        {
            surplus += gas[step] - cost[step];
            total_surplus += gas[step] - cost[step];

            if (surplus < 0)
            {
                surplus = 0;
                start_index = step + 1;
            }
        }

        return (total_surplus < 0) ? -1 : start_index;
    }
};

int main()
{
    vector<int> gas = {1, 2, 3, 4, 5};
    vector<int> cost = {3, 4, 5, 1, 2};

    // vector<int> gas = {2, 3, 4};
    // vector<int> cost = {3, 4, 3};

    // vector<int> gas = {0, 0, 0, 0, 0, 0, 2};
    // vector<int> cost = {0, 0, 0, 0, 0, 1, 0};

    // Solution1 sol;
    Solution2 sol;

    auto answer = sol.run(gas, cost);
    std::cout << answer << std::endl;
}