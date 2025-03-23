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
    ListNode *removeElements(ListNode *head, int val)
    {
        ListNode dummy(0);
        dummy.next = head;
        ListNode *node = &dummy;

        while (node->next != nullptr)
        {
            if (node->next->val == val)
            {
                ListNode *temp = node->next;
                node->next = node->next->next;
                delete temp;
            }
            else
            {
                node = node->next;
            }
        }

        return dummy.next;
    }
};