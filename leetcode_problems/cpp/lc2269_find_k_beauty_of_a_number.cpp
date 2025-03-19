#include <string>
#include <cctype>
using std::string;
using std::to_string;

class Solution
{
public:
    int divisorSubstrings(int num, int k)
    {
        string numStr = to_string(num);
        int n = numStr.size();
        int count = 0;

        for (int i = 0; i <= n - k; i++)
        {
            string subStr = numStr.substr(i, k);
            int subNum = std::stoi(subStr);
            if (subNum != 0 && num % subNum == 0)
            {
                count++;
            }
        }

        return count;
    }
};
