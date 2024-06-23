#include <vector>
#include <iostream>
#include <unordered_map>
using std::vector, std::unordered_map;

class Solution
{
public:
    vector<int> run(vector<int> &numbers, int target)
    {
        unordered_map<int, int> map;
        vector<int> result = {0, 0};

        for (int index = 0; index < numbers.size(); index++)
        {
            map[numbers[index]] = index;
        }

        int index = 0;
        while (index < numbers.size())
        {
            int residue = target - numbers[index];
            auto it = map.find(residue);
            if (it != map.end())
            {
                int index2 = it->second;
                if (index != index2)
                {
                    result[0] = index + 1;
                    result[1] = index2 + 1;
                    return result;
                }
            }
            index++;
        }
        return result;
    }

    vector<int> run2(vector<int> &numbers, int target)
    {
        int p1 = 0;
        int p2 = numbers.size() - 1;
        while (numbers[p1] + numbers[p2] != target)
        {
            if (numbers[p1] + numbers[p2] < target)
            {
                p1++;
            }
            else
            {
                p2--;
            }
        }
        return {p1 + 1, p2 + 1};
    }
};

int main()
{
    vector<int> numbers = {2, 7, 11, 15};
    int target = 9;

    Solution sol;
    vector<int> nums = sol.run(numbers, target);

    for (int num : nums)
    {
        std::cout << num << std::endl;
    }
}