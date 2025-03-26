#include <vector>
#include <string>
#include <algorithm>
#include <functional>
#include <queue>
using std::pair;
using std::priority_queue;
using std::string;
using std::vector;

class SolutionSorting
{
public:
    vector<string> findRelativeRanks(vector<int> &score)
    {
        int n = score.size();
        vector<pair<int, int>> scorePairs;
        for (int i = 0; i < n; ++i)
        {
            scorePairs.push_back({score[i], i});
        }
        std::sort(scorePairs.begin(), scorePairs.end(), std::greater<pair<int, int>>());
        vector<string> result(n);
        for (int i = 0; i < n; ++i)
        {
            if (i == 0)
            {
                result[scorePairs[i].second] = "Gold Medal";
            }
            else if (i == 1)
            {
                result[scorePairs[i].second] = "Silver Medal";
            }
            else if (i == 2)
            {
                result[scorePairs[i].second] = "Bronze Medal";
            }
            else
            {
                result[scorePairs[i].second] = std::to_string(i + 1);
            }
        }
        return result;
    }
};

class SolutionHeap
{
public:
    vector<string> findRelativeRanks(vector<int> &score)
    {
        int n = score.size();
        vector<string> result(n);

        priority_queue<pair<int, int>> maxHeap;
        for (int i = 0; i < n; ++i)
        {
            maxHeap.push({score[i], i});
        }

        for (int i = 0; i < n; ++i)
        {
            auto top = maxHeap.top();
            maxHeap.pop();
            int index = top.second;
            if (i == 0)
            {
                result[index] = "Gold Medal";
            }
            else if (i == 1)
            {
                result[index] = "Silver Medal";
            }
            else if (i == 2)
            {
                result[index] = "Bronze Medal";
            }
            else
            {
                result[index] = std::to_string(i + 1);
            }
        }
        return result;
    }
};
