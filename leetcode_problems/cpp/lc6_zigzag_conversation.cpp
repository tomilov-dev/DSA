#include <string>
#include <iostream>
#include <vector>
using std::string, std::vector;

class Solution
{
public:
    string run(string str, int rows)
    {

        if (rows <= 1)
        {
            return str;
        }

        vector<string> v(rows, "");

        int j = 0;
        int dir = -1;
        for (char chr : str)
        {
            if (j == rows - 1 || j == 0)
                dir *= (-1);

            v[j] += chr;

            if (dir == 1)
                j++;

            else
                j--;
        }

        string res;
        for (auto it : v)
            res += it;

        return res;
    }
};

int main()
{

    string str = "PAYPALISHIRING";
    int rows = 3;

    Solution sol;
    string answer = sol.run(str, rows);

    std::cout << answer << std::endl;
}