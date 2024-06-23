#include <vector>
#include <unordered_map>
#include <iostream>
using std::unordered_map;
using std::vector;

class Solution
{
public:
    vector<int> run(vector<int> numbers, int target)
    {
        unordered_map<int, int> searched;

        for (int index = 0; index < numbers.size(); index++)
        {
            int search = target - numbers[index];
            if (searched.find(search) != searched.end())
            {
                return {index, searched.at(search)};
            }
            else
            {
                searched[numbers[index]] = index;
            }
        }

        return {};
    }
};

int main()
{
    vector<int> numbers = {2,
                           7,
                           11,
                           15};
    int target = 9;

    Solution sol;
    vector<int> answer = sol.run(numbers, 9);

    for (int num : answer)
    {
        std::cout << num << std::endl;
    }

    return 0;
}