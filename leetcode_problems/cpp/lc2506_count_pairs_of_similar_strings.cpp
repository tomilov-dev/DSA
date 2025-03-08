#include <string>
#include <vector>
#include <map>
#include <set>
#include <unordered_map>
#include <iostream>
using std::map;
using std::set;
using std::string;
using std::unordered_map;
using std::vector;

class Solution
{
public:
    int similarPairs(vector<string> &words)
    {
        int count = 0;
        vector<vector<bool>> word_chars(words.size(), vector<bool>(26, false));
        for (int i = 0; i < words.size(); i++)
        {
            string word = words[i];
            for (char chr : word)
            {
                word_chars[i][chr - 'a'] = true;
            }
        }

        for (int i = 0; i < word_chars.size(); i++)
        {
            for (int j = i + 1; j < word_chars.size(); j++)
            {
                if (word_chars[i] == word_chars[j])
                {
                    count++;
                }
            }
        }

        return count;
    }
};

class Solution2
{
public:
    int similarPairs(vector<string> &words)
    {
        int count = 0;
        map<set<char>, int> word_sets;

        for (const string &word : words)
        {
            set<char> char_set(word.begin(), word.end());
            word_sets[char_set]++;
        }

        for (const auto &pair : word_sets)
        {
            int n = pair.second;
            count += (n * (n - 1)) / 2;
        }

        return count;
    }
};

class Solution3
{
public:
    int similarPairs(vector<string> &words)
    {
        int count = 0;
        unordered_map<int, int> word_masks;

        for (const string &word : words)
        {
            int mask = 0;
            for (char chr : word)
            {
                mask |= (1 << (chr - 'a'));
            }
            word_masks[mask]++;
        }

        for (const auto &pair : word_masks)
        {
            int n = pair.second;
            count += (n * (n - 1)) / 2;
        }

        return count;
    }
};

int main()
{
    vector<string> words = {"abc", "bca", "cab", "xyz", "zyx"};
    Solution sol;
    int result = sol.similarPairs(words);
    std::cout << result << std::endl;
    return 0;
}