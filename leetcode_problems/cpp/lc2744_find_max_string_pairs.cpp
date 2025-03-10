#include <vector>
#include <string>
#include <unordered_map>
#include <iostream>
using std::string;
using std::unordered_map;
using std::vector;

class Solution
{
public:
    string reverse(string word)
    {
        return string(word.rbegin(), word.rend());
    }

    int maximumNumberOfStringPairs(vector<string> &words)
    {
        unordered_map<string, int> map;
        int res = 0;
        for (string word : words)
        {
            string rev = reverse(word);
            res += map[word];
            map[rev]++;
        }
        return res;
    }
};

int main()
{
    vector<string> words = {"cd", "ac", "dc", "ca", "zz"};
    Solution sol;
    std::cout << sol.maximumNumberOfStringPairs(words) << std::endl;
    return 0;
}