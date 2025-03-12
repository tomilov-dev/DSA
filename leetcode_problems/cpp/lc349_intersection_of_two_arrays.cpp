#include <vector>
#include <algorithm>
using std::vector;

class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        std::sort(nums1.begin(), nums1.end());
        std::sort(nums2.begin(), nums2.end());
        int p1 = 0;
        int p2 = 0;
        vector<int> res;
        while (p1 < nums1.size() && p2 < nums2.size()) {
            if (nums1[p1] < nums2[p2]) {
                p1++;
            } else if (nums1[p1] > nums2[p2]) {
                p2++;
            } else {
                if (res.empty() || res.back() != nums1[p1]) {
                    res.push_back(nums1[p1]);
                }
                p1++;
                p2++;
            }
        }
        return res;
    }
};

int main() {
    vector<int> nums1 = {1, 2, 2, 1};
    vector<int> nums2 = {2, 2};
    Solution sol;
    vector<int> result = sol.intersection(nums1, nums2);
    for (int num : result) {
        std::cout << num << " ";
    }
    return 0;
}