class Solution
{
public:
    void backtrack(int cur, int *arr, int n, int &count)
    {
        if (cur > n)
        {
            ++count;
        }

        for (int i = 0; i < n; i++)
        {
            if (arr[i] != 0)
            {
                continue;
            }
            if (cur % (i + 1) != 0 && (i + 1) % cur != 0)
            {
                continue;
            }

            arr[i] = cur;
            backtrack(cur + 1, arr, n, count);
            arr[i] = 0;
        }
    }

    int countArrangement(int n)
    {
        int count = 0;
        int *arr = new int[n]();
        backtrack(1, arr, n, count);
        delete[] arr;
        return count;
    }
};
