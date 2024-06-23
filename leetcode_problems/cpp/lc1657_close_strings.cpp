#include <unordered_map>
#include <unordered_set>
#include <string>
#include <iostream>
#include <vector>
#include <algorithm>
using std::string, std::vector;

class Solution
{
public:
    bool run(string word1, string word2)
    {
        if (word1.length() != word2.length())
        {
            return false;
        }

        std::unordered_map<char, int> m1;
        std::unordered_map<char, int> m2;

        int index = 0;
        while (index < word1.length())
        {
            m1[word1[index]]++;
            m2[word2[index]]++;
            index++;
        }

        std::unordered_map<int, int> counts;
        for (auto &pair : m1)
        {
            if (m2.find(pair.first) == m2.end())
            {
                return false;
            }
            counts[pair.second]++;
        }

        for (auto &pair : m2)
        {
            counts[pair.second]--;
            if (counts[pair.second] < 0)
            {
                return false;
            }
        }

        return true;
    }

    bool run2(string word1, string word2)
    {
        if (word1.length() != word2.length())
        {
            return false;
        }

        vector<int> counts1(26, 0), counts2(26, 0);
        vector<int> chars1(26, 0), chars2(26, 0);

        int index = 0;
        while (index < word1.length())
        {
            counts1[word1[index] - 'a']++;
            chars1[word1[index] - 'a'] = 1;

            counts2[word2[index] - 'a']++;
            chars2[word2[index] - 'a'] = 1;

            index++;
        }

        std::sort(counts1.begin(), counts1.end());
        std::sort(counts2.begin(), counts2.end());

        return counts1 == counts2 && chars1 == chars2;
    }
};

int main()
{
    string word1 = "aaabbbbccddeeeeefffff", word2 = "aaaaabbcccdddeeeeffff";

    Solution sol;
    bool answer = sol.run2(word1, word2);

    std::cout << answer << std::endl;
}