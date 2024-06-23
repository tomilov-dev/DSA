#include <string>
#include <iostream>
#include <vector>
#include <utility>
using std::string, std::vector, std::pair;

class Solution
{
public:
    template <typename T>
    void print(T value)
    {
        std::cout << value << std::endl;
    }

    vector<pair<int, string>> romans = {
        {1000, "M"},
        {900, "CM"},
        {500, "D"},
        {400, "CD"},
        {100, "C"},
        {90, "XC"},
        {50, "L"},
        {40, "XL"},
        {10, "X"},
        {9, "IX"},
        {5, "V"},
        {4, "IV"},
        {1, "I"},
    };

    string run(int num)
    {
        string roman = "";
        int point = 0;

        while (num > 0)
        {
            while (num / romans[point].first <= 0 &&
                   num < romans[point].first)
            {
                point++;
            }

            num -= romans[point].first;
            roman += romans[point].second;
        }

        return roman;
    }

    string run2(int num)
    {
        string ones[] = {"", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"};
        string tens[] = {"", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"};
        string hrns[] = {"", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"};
        string ths[] = {"", "M", "MM", "MMM"};

        return ths[num / 1000] + hrns[(num % 1000) / 100] + tens[(num % 100) / 10] + ones[num % 10];
    }
};

int main()
{
    int num = 3000;

    Solution sol;
    string answer = sol.run(num);

    std::cout << answer << std::endl;
}