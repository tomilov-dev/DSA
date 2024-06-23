#include <string>
#include <unordered_map>
#include <iostream>
using std::string, std::unordered_map;

class Solution
{
public:
    bool run(string pattern, string str)
    {
        unordered_map<char, string> map1;
        unordered_map<string, char> map2;

        int ipt = 0;
        int index = 0;
        while (index < str.size())
        {
            string word = "";
            while (index < str.size() &&
                   str[index] != ' ')
            {
                word += str[index++];
            }

            char pt = pattern[ipt++];

            auto it1 = map1.find(pt);
            auto it2 = map2.find(word);
            bool empt1 = it1 == map1.end();
            bool empt2 = it2 == map2.end();
            if (empt1)
            {
                if (empt2)
                {
                    map1[pt] = word;
                    map2[word] = pt;
                }
                else
                {
                    return false;
                }
            }
            else
            {
                if (empt2)
                {
                    return false;
                }
                else
                {
                    if (pt != it2->second ||
                        word != it1->second)
                    {
                        return false;
                    }
                }
            }

            index++;
        }

        return ipt == pattern.size();
    }
};

int main()
{
    // string pattern = "abba";
    // string str = "dog cat cat dog";

    // string pattern = "abba";
    // string str = "dog cat cat fish";

    // string pattern = "aaaa";
    // string str = "dog cat cat dog";

    string pattern = "jquery";
    string str = "jquery";

    Solution sol;
    bool answer = sol.run(pattern, str);

    std::cout << answer << std::endl;
}