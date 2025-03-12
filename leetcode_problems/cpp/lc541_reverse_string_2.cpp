#include <string>
#include <algorithm>
using std::string;

class Solution {
public:
    void reverseSubStr(string &s, int p1, int p2) {
        while (p1 < p2) {
            char temp = s[p1];
            s[p1] = s[p2];
            s[p2] = temp;
            p1++;
            p2--;
        }
    }

    string reverseStr(string s, int k) {
        for (int i = 0; i < s.size(); i += 2 * k) {
            int p1 = i;
            int p2 = std::min(i + k - 1, static_cast<int>(s.size() - 1));
            reverseSubStr(s, p1, p2);
        }
        return s;
    }
};

int main() {
    string s = "abcdefg";
    int k = 2;
    Solution sol;
    string res = sol.reverseStr(s, k);
    return 0;
}