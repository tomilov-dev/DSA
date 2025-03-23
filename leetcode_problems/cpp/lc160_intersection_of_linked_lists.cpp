struct ListNode
{
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
};

class Solution
{
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB)
    {
        ListNode *node1 = headA;
        ListNode *node2 = headB;
        while (node1 != node2)
        {
            node1 = node1 == nullptr ? headB : node1->next;
            node2 = node2 == nullptr ? headA : node2->next;
        }
        return node1;
    }
};
