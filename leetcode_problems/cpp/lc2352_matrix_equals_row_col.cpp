#include <vector>
#include <algorithm>
#include <iostream>
#include <numeric>
using std::vector;

class Solution
{
public:
    int run(vector<vector<int>> &matrix)
    {
        int count = 0;
        vector<vector<int>> cols;

        for (int col_index = 0; col_index < matrix[0].size(); col_index++)
        {
            vector<int> col;
            for (int row_index = 0; row_index < matrix.size(); row_index++)
            {
                col.push_back(matrix[row_index][col_index]);
            }
            cols.push_back(col);
        }

        for (int row_index = 0; row_index < matrix.size(); row_index++)
        {
            for (int col_index = 0; col_index < matrix[0].size(); col_index++)
            {
                if (matrix[row_index] == cols[col_index])
                {
                    count++;
                }
            }
        }

        return count;
    }
};

int main()
{
    vector<vector<int>> matrix = {{3, 1, 2, 2}, {1, 4, 4, 5}, {2, 4, 2, 2}, {2, 4, 2, 2}};

    Solution sol;
    auto answer = sol.run(matrix);

    std::cout << answer << std::endl;
}