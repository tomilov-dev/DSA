#include <vector>
#include <string>
#include <iostream>
#include <functional>
#include <unordered_map>
using std::vector, std::string, std::unordered_map, std::hash;

class Solution
{
public:
    string strId(string str)
    {
        const int N = 26;
        int arr[N] = {};
        string id = "";

        for (char chr : str)
        {
            arr[chr - 'a']++;
        }

        for (int index = 0; index < N; index++)
        {
            id += string(arr[index], index + 'a');
        }

        return id;
    }

    vector<vector<string>> run(vector<string> &strs)
    {
        vector<vector<string>> output;
        unordered_map<string, vector<string>> map;

        for (string str : strs)
        {
            string id = strId(str);
            map[id].push_back(str);
        }

        for (auto it = map.begin(); it != map.end(); it++)
        {
            output.push_back(it->second);
        }

        return output;
    }
};

int main()
{
    vector<string> strs = {"eat", "tea", "tan", "ate", "nat", "bat"};

    Solution sol;
    auto answer = sol.run(strs);

    for (auto group : answer)
    {
        std::cout << "[";
        for (auto word : group)
        {
            std::cout << word << ", ";
        }
        std::cout << "]" << std::endl;
    }
}