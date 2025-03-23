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
    ListNode *getMiddle(ListNode *head)
    {
        ListNode *slow = head;
        ListNode *fast = head;
        while (fast != nullptr && fast->next != nullptr)
        {
            slow = slow->next;
            fast = fast->next->next;
        }
        return slow;
    }

    ListNode *reverseNode(ListNode *head)
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

    bool isPalindrome(ListNode *head)
    {
        ListNode *middle = getMiddle(head);
        middle = reverseNode(middle);
        while (middle != nullptr && head != nullptr)
        {
            if (middle->val != head->val)
            {
                return false;
            }
            middle = middle->next;
            head = head->next;
        }
        return true;
    }
};
