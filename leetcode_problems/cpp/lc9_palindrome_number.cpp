#include <iostream>
#include <string>
using std::string;

class Solution1
{
public:
    bool run(int num)
    {
        string str = std::to_string(num);

        int p1 = 0;
        int p2 = str.size() - 1;

        while (p1 < p2)
        {
            if (str[p1++] != str[p2--])
            {
                return false;
            }
        }

        return true;
    }
};

class Solution2
{
public:
    bool run(int num)
    {
        if (num < 0)
        {
            return false;
        }

        long reversed = 0;
        int temp = num;
        while (temp != 0)
        {
            int digit = temp % 10;
            reversed = reversed * 10 + digit;
            temp /= 10;
        }

        return (num == reversed);
    }
};

int main()
{
    int num = 121;

    Solution1 sol1;
    Solution2 sol2;

    // bool answer = sol1.run(num);
    bool answer = sol2.run(num);

    std::cout << answer << std::endl;
}