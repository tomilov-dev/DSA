#include <string>
#include <iostream>
using std::string;

class Solution
{
public:
    void str_swap(string &str, int p1, int p2)
    {
        while (p1 < p2)
        {
            char temp = str[p1];
            str[p1++] = str[p2];
            str[p2--] = temp;
        }
    }

    string run(string str)
    {
        int p1 = 0;
        int p2 = str.length() - 1;
        str_swap(str, p1, p2);

        p1 = 0;
        p2 = 0;
        int index = 0;
        while (index < str.length())
        {
            while (index < str.length() && str[index] != ' ')
            {
                str[p2++] = str[index++];
            }

            if (p1 < p2)
            {
                str_swap(str, p1, p2 - 1);
                if (p2 < str.length())
                {
                    str[p2++] = ' ';
                }
                p1 = p2;
            }

            index++;
        }

        while (p2 < str.length())
        {
            str.pop_back();
        }

        p1 = str.length() - 1;
        while (p1 < str.length() && str[p1] == ' ')
        {
            str.pop_back();
            p1--;
        }

        return str;
    }
};

int main()
{
    // string str = "  run   this   case    please   ";
    // string str = "blue is sky the";
    // string str = "  hello world  ";
    // string str = "a good   example";
    string str = " asdasd df f";

    Solution sol;
    string answer = sol.run(str);

    std::cout << '"' << answer << '"' << std::endl;
}