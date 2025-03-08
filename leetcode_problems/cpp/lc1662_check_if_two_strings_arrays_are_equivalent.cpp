#include <vector>
#include <string>
#include <iostream>
using std::string;
using std::vector;

class Solution
{
public:
    bool arrayStringsAreEqual(vector<string> &word1, vector<string> &word2)
    {
        int ap1 = 0;
        int wp1 = 0;
        int ap2 = 0;
        int wp2 = 0;
        while (ap1 < word1.size() && ap2 < word2.size())
        {
            char chr1 = word1[ap1][wp1];
            char chr2 = word2[ap2][wp2];
            if (chr1 != chr2)
            {
                std::cout << "exit " << chr1 << " " << chr2 << std::endl;
                return false;
            }
            wp1++;
            wp2++;

            if (wp1 >= word1[ap1].size())
            {
                ap1++;
                wp1 = 0;
            }

            if (wp2 >= word2[ap2].size())
            {
                ap2++;
                wp2 = 0;
            }
        }
        return ap1 == word1.size() && ap2 == word2.size();
    }
};

int main()
{
    vector<string> word1 = {"ab", "c"};
    vector<string> word2 = {"a", "bc"};
    Solution sol;
    std::cout << sol.arrayStringsAreEqual(word1, word2) << std::endl;
    return 0;
}