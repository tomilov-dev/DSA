#include <vector>
#include <iostream>
#include <limits>
using std::vector;

class Solution
{
public:
    double average(vector<int> &salary)
    {
        int maxi = std::numeric_limits<int>::min();
        int mini = std::numeric_limits<int>::max();
        int sum = 0;
        for (int i = 0; i < salary.size(); i++)
        {

            int cur = salary[i];
            if (cur > maxi)
            {
                maxi = cur;
            }
            if (cur < mini)
            {
                mini = cur;
            }
            sum += cur;
        }
        sum -= mini;
        sum -= maxi;
        return static_cast<double>(sum) / (salary.size() - 2);
    }
};

int main()
{
    // vector<int> salary = {4000, 3000, 1000, 2000};
    vector<int> salary = {1000, 2000, 3000};
    Solution sol;
    double result = sol.average(salary);
    std::cout << result << std::endl;
    return 0;
}