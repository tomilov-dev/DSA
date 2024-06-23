#include <string>
#include <iostream>
#include <unordered_map>
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

        std::unordered_map<char, char> map1;
        std::unordered_map<char, char> map2;

        int index = 0;
        while (index < s.size())
        {
            auto it1 = map1.find(s[index]);
            auto it2 = map2.find(t[index]);

            bool empt1 = it1 == map1.end();
            bool empt2 = it2 == map2.end();

            if (empt1)
            {
                if (empt2)
                {
                    map1[s[index]] = t[index];
                    map2[t[index]] = s[index];
                }
                else
                {
                    return false;
                }
            }
            else
            {
                if (!empt1 && !empt2)
                {
                    if (it1->second != t[index] &&
                        it2->second != s[index])
                    {
                        std::cout << "here" << std::endl;
                        return false;
                    }
                }
                else
                {
                    return false;
                }
            }
            index++;
        }

        return true;
    }
};

int main()
{
    // string s = "egg";
    // string t = "add";

    // string s = "foo";
    // string t = "bar";

    // string s = "paper";
    // string t = "title";

    string s = "badc";
    string t = "baba";

    Solution sol;
    bool answer = sol.run(s, t);
    std::cout << answer << std::endl;
}