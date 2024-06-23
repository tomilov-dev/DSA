#include <string>
#include <iostream>
using std::string;

class Solution
{
public:
    bool run(string s, string t)
    {
        if (s.size() != t.size())
        {
            return false;
        }

        const int N = 26;
        int mp1[N] = {};
        int mp2[N] = {};

        for (int index = 0; index < s.size(); index++)
        {
            mp1[s[index] - 'a']++;
            mp2[t[index] - 'a']++;
        }

        for (int index = 0; index < N; index++)
        {
            if (mp1[index] != mp2[index])
            {
                return false;
            }
        }

        return true;
    }
};

int main()
{
    string s = "anagram";
    string t = "nagaram";

    Solution sol;
    bool answer = sol.run(s, t);

    std::cout << answer << std::endl;
}