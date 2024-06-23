#include <vector>
#include <iostream>
#include <functional>
#include <numeric>
using std::vector;

class Solution
{
public:
    int find(vector<int> &row)
    {
        int index = 0;
        while (index < row.size() && row[index] == 0)
        {
            index++;
        }

        return index;
    }

    int col_sum(vector<vector<int>> &matrix, int col_index)
    {
        int sum = 0;
        for (int i = 0; i < matrix.size(); i++)
        {
            sum += matrix[i][col_index];
        }
        return sum;
    }

    int run(vector<vector<int>> &matrix)
    {
        int count = 0;
        for (int index = 0; index < matrix.size(); index++)
        {
            vector<int> row = matrix[index];
            int check = std::accumulate(row.begin(), row.end(), 0);

            if (check == 1)
            {
                int col_index = find(row);
                check = col_sum(matrix, col_index);
                if (check == 1)
                {
                    count += 1;
                }
            }
        }

        return count;
    }
};

int main()
{
    vector<vector<int>> matrix = {{1, 0, 0},
                                  {0, 0, 1},
                                  {1, 0, 0}};

    Solution sol;
    int count = sol.run(matrix);

    std::cout << count << std::endl;
    return 0;
}