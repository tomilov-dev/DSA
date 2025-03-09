#include <vector>
#include <iostream>
#include <unordered_map>
using std::unordered_map;
using std::vector;

class Solution
{
public:
    bool canFormArray(vector<int> &arr, vector<vector<int>> &pieces)
    {
        unordered_map<int, int> map;
        for (int i = 0; i < arr.size(); i++)
        {
            map[arr[i]] = i;
        }
        for (const auto &piece : pieces)
        {
            if (map.find(piece[0]) == map.end())
            {
                return false;
            }
            int prev = map[piece[0]];
            for (int j = 1; j < piece.size(); j++)
            {
                if (map.find(piece[j]) == map.end() || map[piece[j]] != prev + 1)
                {
                    return false;
                }
                prev = map[piece[j]];
            }
        }
        return true;
    }
};
