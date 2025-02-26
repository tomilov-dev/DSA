#include <vector>
#include <string>
#include <iostream>
#include <sstream>
using std::string;
using std::vector;

class Solution
{
public:
    vector<string> splitWordsBySeparator(vector<string> &words, char sep)
    {
        vector<string> result = {};
        for (int i = 0; i < words.size(); i++)
        {
            string word = words[i];
            string cur_word = "";
            for (int j = 0; j < word.size(); j++)
            {
                char cur_char = word[j];
                if (cur_char == sep)
                {
                    if (cur_word.size() > 0)
                    {
                        result.push_back(cur_word);
                    }
                    cur_word = "";
                }
                else
                {
                    cur_word.push_back(cur_char);
                }

                if (j == word.size() - 1 && cur_word.size() > 0)
                {
                    result.push_back(cur_word);
                }
            }
        }
        return result;
    }
};

class Solution2
{
public:
    vector<string> splitWordsBySeparator(vector<string> &words, char sep)
    {
        vector<string> result;
        for (const auto &word : words)
        {
            std::stringstream ss(word);
            string item;
            while (std::getline(ss, item, sep))
            {
                if (!item.empty())
                {
                    result.push_back(item);
                }
            }
        }
        return result;
    }
};

int main()
{
    vector<string> words = {"one.two.three", "four.five", "six"};
    char sep = '.';
    Solution2 sol;
    auto result = sol.splitWordsBySeparator(words, sep);
    for (int i = 0; i < result.size(); i++)
    {
        std::cout << result[i] << std::endl;
    }
    return 0;
}