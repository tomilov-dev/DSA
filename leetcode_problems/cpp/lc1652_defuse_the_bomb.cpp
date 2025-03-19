#include <vector>
using std::vector;

class Solution
{
public:
    int index(int i, int k, int n)
    {
        if (k > 0)
        {
            return (i + k) % n;
        }
        else
        {
            return (i + k + n) % n;
        }
    }

    vector<int> decrypt(vector<int> &code, int k)
    {
        int n = code.size();
        if (k == 0)
        {
            return vector<int>(n, 0);
        }
        vector<int> res(n, 0);
        int sum = 0;
        int start = k > 0 ? 1 : k;
        int end = k > 0 ? k : -1;
        for (int i = start; i <= end; i++)
        {
            sum += code[index(0, i, n)];
        }
        for (int i = 0; i < n; i++)
        {
            res[i] = sum;
            sum -= code[index(i, start, n)];
            sum += code[index(i, end + 1, n)];
        }
        return res;
    }
};