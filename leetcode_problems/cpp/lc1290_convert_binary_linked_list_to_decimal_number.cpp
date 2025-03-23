#include <cmath>

struct ListNode
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution
{
public:
    ListNode *reverse(ListNode *head)
    {
        ListNode *prev = nullptr;
        ListNode *cur = head;
        while (cur != nullptr)
        {
            ListNode *temp = cur->next;
            cur->next = prev;
            prev = cur;
            cur = temp;
        }
        return prev;
    }

    int getDecimalValue(ListNode *head)
    {
        int res = 0;
        while (head != nullptr)
        {
            res = (res << 1) | head->val;
            head = head->next;
        }
        return res;
    }
};
