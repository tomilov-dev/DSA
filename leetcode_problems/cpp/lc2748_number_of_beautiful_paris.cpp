#include <vector>
#include <iostream>
#include <numeric>
#include <unordered_map>
using std::gcd;
using std::unordered_map;
using std::vector;

class Solution
{
public:
    int first_digit(int num)
    {
        while (num >= 10)
        {
            num /= 10;
        }
        return num;
    }

    int last_digit(int num)
    {
        return num % 10;
    }

    int countBeautifulPairs(vector<int> &nums)
    {
        int res = 0;
        for (int i = 0; i < nums.size(); i++)
        {
            for (int j = i + 1; j < nums.size(); j++)
            {
                int cur_gcd = gcd(first_digit(nums[i]), last_digit(nums[j]));
                res += cur_gcd == 1;
            }
        }
        return res;
    }

    int countBeautifulPairs2(vector<int> &nums)
    {
        unordered_map<int, int> first_digit_count;
        int res = 0;

        for (int num : nums)
        {
            int last = last_digit(num);
            for (const auto &entry : first_digit_count)
            {
                if (gcd(entry.first, last) == 1)
                {
                    res += entry.second;
                }
            }
            first_digit_count[first_digit(num)]++;
        }

        return res;
    }
};

int main()
{
    return 0;
}