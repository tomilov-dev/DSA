#include <vector>
#include <iostream>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>
#include <iterator>

class Solution
{
public:
    bool run(std::vector<int> &array)
    {
        std::unordered_map<int, int> mapper;
        std::unordered_set<int> uniqs;

        for (int num : array)
        {
            mapper[num]++;
        }

        for (auto kv = mapper.begin(); kv != mapper.end(); kv++)
        {
            auto pair = *kv;
            auto occurence = pair.second;

            if (uniqs.find(occurence) == uniqs.end())
            {
                uniqs.insert(occurence);
            }
            else
            {
                return false;
            }
        }

        return true;
    }

    bool run2(std::vector<int> &array)
    {

        std::unordered_map<int, int> mapper;
        std::unordered_set<int> uniqs;

        for (int num : array)
            mapper[num]++;
        for (auto &pair : mapper)
            uniqs.insert(pair.second);
        return mapper.size() == uniqs.size();
    }

    bool run3(std::vector<int> &array)
    {
        short mem[2001] = {};

        for (auto num : array)
        {
            ++mem[num + 1000];
        }
        std::sort(std::begin(mem), std::end(mem));

        for (int index = 1; index < 2001; index++)
        {
            if (mem[index] && mem[index] == mem[index - 1])
            {
                return false;
            }
        }

        return true;
    }
};

int main()
{
    std::vector<int> array = {1, 2, 2, 1, 1, 3};

    Solution sol;
    bool answer = sol.run3(array);

    std::cout << answer << std::endl;
}