#include <vector>
#include <iostream>
#include <algorithm>
using std::vector, std::max;

class Solution
{
public:
    void print(vector<int> nums)
    {
        for (int num : nums)
        {
            std::cout << num << std::endl;
        }
    }

    int run(vector<int> &ratings)
    {
        int total = 0;
        vector<int> left(ratings.size(), 1);
        vector<int> right(ratings.size(), 1);

        for (int index = 1; index < ratings.size(); index++)
        {
            if (ratings[index - 1] < ratings[index])
            {
                left[index] = left[index - 1] + 1;
            }
        }

        for (int index = ratings.size() - 2; index >= 0; index--)
        {
            if (ratings[index + 1] < ratings[index])
            {
                right[index] = right[index + 1] + 1;
            }
        }

        for (int index = 0; index < ratings.size(); index++)
        {
            total += max(left[index], right[index]);
        }

        return total;
    }

    int run2(vector<int> &ratings)
    {
        int total = 0;
        vector<int> candies(ratings.size(), 1);

        for (int index = 1; index < ratings.size(); index++)
        {
            if (ratings[index - 1] < ratings[index])
            {
                candies[index] = candies[index - 1] + 1;
            }
        }

        total += candies[candies.size() - 1];
        for (int index = ratings.size() - 2; index >= 0; index--)
        {
            int curmax = candies[index];
            if (ratings[index + 1] < ratings[index])
            {
                int localmax = candies[index + 1] + 1;
                curmax = max(curmax, localmax);
                candies[index] = curmax;
            }
            total += curmax;
        }

        return total;
    }
};

int main()
{
    // vector<int> ratings = {1, 1, 3, 1, 0, 5};
    // vector<int> ratings = {1, 0, 2};
    // vector<int> ratings = {1, 2, 2};
    vector<int> ratings = {1, 3, 4, 5, 2};

    Solution sol;
    auto answer = sol.run2(ratings);

    std::cout << "answer is " << answer << std::endl;
}