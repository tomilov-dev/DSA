#include <string>
using std::string;

class Solution {
public:
    void reverse_word(string &s, int p1, int p2) {
        while (p1 < p2) {
            char temp = s[p1];
            s[p1] = s[p2];
            s[p2] = temp;
            p1++;
            p2--;
        }
    }

    string reverseWords(string s) {
        int p1 = 0;
        int p2 = 0;
        while (p1 < s.size() && p2 < s.size()) {
            while (p2 < s.size() && s[p2] != ' ') {
                p2++;
            }
            reverse_word(s, p1, p2 - 1);
            p1 = p2 + 1;
            p2 = p1;
        }
        return s;
    }
};

int main() {
    string s = "Let's take LeetCode contest";
    Solution sol;
    string res = sol.reverseWords(s);
    return 0;
}