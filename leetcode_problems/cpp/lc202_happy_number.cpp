#include <iostream>
#include <unordered_map>
using std::unordered_map;

class Solution
{
public:
    int sqr(int n)
    {
        int sqr = 0;
        while (n > 0)
        {
            int prt = n % 10;
            sqr += prt * prt;
            n /= 10;
        }

        return sqr;
    }

    bool run(int n)
    {
        int slow = n;
        int fast = n;
        do
        {
            slow = sqr(slow);
            fast = sqr(fast);
            fast = sqr(fast);
        } while (slow != fast);

        if (slow == 1)
        {
            return true;
        }
        else
        {
            return false;
        }
    }

    bool run2(int n)
    {
        unordered_map<int, int> map;
        int prev;
        while (n != 1)
        {
            auto it = map.find(n);
            prev = n;
            if (it == map.end())
            {
                n = sqr(n);
                map[prev] = n;
            }
            else
            {
                return false;
            }
        }
        return true;
    }
};

int main()
{
    int n = 19;

    Solution sol;
    bool answer = sol.run(n);

    std::cout << answer << std::endl;
}