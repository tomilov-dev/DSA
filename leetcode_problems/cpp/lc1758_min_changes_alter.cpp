#include <string>
#include <iostream>
#include <algorithm>

class Solution
{
public:
    int run(std::string str)
    {
        int start0 = 0;
        int start1 = 0;

        for (int index = 0; index < str.length(); index++)
        {
            if (index % 2 == 0)
            {
                if (str[index] == '0')
                {
                    start1++;
                }
                else
                {
                    start0++;
                }
            }
            else
            {
                if (str[index] == '1')
                {
                    start1++;
                }
                else
                {
                    start0++;
                }
            }
        }

        return std::min(start0, start1);
    }

    int run2(std::string str)
    {
        int f0 = 0;
        int f1 = 1;
        int count0 = 0;
        int count1 = 0;
        for (char chr : str)
        {
            count0 += chr - '0' != f1;
            count1 += chr - '0' != f0;
            std::swap(f0, f1);
        }

        return std::min(count0, count1);
    }
};

int main()
{
    std::string str = "10010100";

    Solution sol;
    int answer = sol.run2(str);

    std::cout << answer << std::endl;
}