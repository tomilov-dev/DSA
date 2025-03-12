#include <string>
#include <iostream>
#include <unordered_map>
using std::string;
using std::unordered_map;

class Solution {
public:
    string reverseVowels(string s) {
            unordered_map<char, bool> vow = {
                {'A', true},
                {'a', true},
                {'E', true},
                {'e', true},
                {'I', true},
                {'i', true},
                {'O', true},
                {'o', true},
                {'U', true},
                {'u', true},
            };
            int p1 = 0;
            int p2 = s.size() - 1;
            while (p1 < p2) {
                while (p1 < p2 && p1 < s.size() && !vow[s[p1]]) {
                    p1++;
                }
                while (p1 < p2 && p2 >= 0 && !vow[s[p2]]) {
                    p2--;
                }
                if (p1 >= p2) {
                    break;
                }
                char temp = s[p1];
                s[p1] = s[p2];
                s[p2] = temp;
                p1++;
                p2--;
            }
            return s;
    }
};

int main() {
    string s = "IceCreAm";
    Solution sol;
    auto res = sol.reverseVowels(s);
    std::cout << res << std::endl;
}