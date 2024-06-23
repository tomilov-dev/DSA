#include <vector>
#include <iostream>
using std::vector;

class Solution
{
public:
    vector<vector<int>> run(vector<vector<int>> &matrix)
    {
        vector<int> row(matrix.size());
        vector<int> col(matrix[0].size());

        for (int i = 0; i < matrix.size(); i++)
        {
            for (int j = 0; j < matrix[0].size(); j++)
            {
                row[i] += matrix[i][j];
                col[j] += matrix[i][j];
            }
        }

        vector<vector<int>> diff(matrix.size(), vector<int>(matrix[0].size()));
        for (int i = 0; i < matrix.size(); i++)
        {
            for (int j = 0; j < matrix[0].size(); j++)
            {
                diff[i][j] = 2 * row[i] + 2 * col[j] - matrix.size() - matrix[0].size();
            }
        }

        return diff;
    }
};

int main()
{
    vector<vector<int>> matrix = {
        {0, 1, 1},
        {1, 0, 1},
        {0, 0, 1},
    };

    Solution sol;

    matrix = sol.run(matrix);
}