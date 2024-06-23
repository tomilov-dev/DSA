#include <queue>
#include <iostream>
using std::queue;

class RecentCounter
{
public:
    queue<int> requests;
    RecentCounter()
    {
    }

    int ping(int t)
    {
        requests.push(t);
        while (requests.front() < t - 3000)
        {
            requests.pop();
        }
        return requests.size();
    }
};

int main()
{
    RecentCounter *obj = new RecentCounter();
    obj->ping(1);
    obj->ping(2);
}