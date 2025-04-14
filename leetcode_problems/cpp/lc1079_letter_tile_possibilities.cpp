#include <string>
using std::string;

class Solution
{
public:
    void backtrack(int arr[], int &count)
    {
        for (int i = 0; i < 26; i++)
        {
            if (arr[i] <= 0)
            {
                continue;
            }

            arr[i]--;
            count++;
            backtrack(arr, count);
            arr[i]++;
        }
    }

    int numTilePossibilities(string tiles)
    {
        int count = 0;
        int *arr = new int[26]();
        for (char chr : tiles)
        {
            arr[chr - 'A']++;
        }
        backtrack(arr, count);
        return count;
    }
};