#include <vector>
#include <iostream>
#include <algorithm>
#include <set>
using std::vector;

class Solution
{
public:
    int run(vector<vector<int>> &points)
    {
        std::set<int> mapper;
        int max_w = 0;

        for (vector<int> &point : points)
        {
            mapper.insert(point[0]);
        }

        for (auto it = next(begin(mapper)); it != end(mapper); it++)
        {
            max_w = std::max(max_w, *it - *prev(it));
        }

        return max_w;
    }
};

int main()
{
    vector<vector<int>> points = {{8, 7},
                                  {9, 9},
                                  {7, 4},
                                  {9, 7}};

    Solution sol;

    int answer = sol.run(points);

    std::cout << answer << std::endl;
}