#include <string>
#include <iostream>
#include <algorithm>
using std::string;

class Solution
{
public:
    int run(string str)
    {
        int sum = 0;
        int cur_sum = 0;
        for (int index = 0; index < str.length() - 1; index++)
        {
            cur_sum = 0;
            for (int p1 = 0; p1 <= index; p1++)
            {
                if (str[p1] == '0')
                {
                    cur_sum++;
                }
            }

            for (int p2 = index + 1; p2 < str.length(); p2++)
            {
                if (str[p2] == '1')
                {
                    cur_sum++;
                }
            }
            sum = std::max(sum, cur_sum);
        }

        return sum;
    }

    int run2(string str)
    {
        int right_ones = 0, left_zeroes = 0;
        for (char chr : str)
        {
            if (chr == '1')
            {
                right_ones++;
            }
        }

        int sum = 0;
        for (int index = 0; index < str.length() - 1; index++)
        {
            if (str[index] == '0')
            {
                left_zeroes++;
            }
            else
            {
                right_ones--;
            }

            sum = std::max(sum, left_zeroes + right_ones);
        }
        return sum;
    }
};

int main()
{
    string str = "00111";

    Solution sol;
    int answer = sol.run2(str);

    std::cout << answer << std::endl;
}