#include <vector>
using std::vector;

class Solution
{
public:
    vector<vector<int>> flipAndInvertImage(vector<vector<int>> &image)
    {
        int n = image.size();
        int m = image[0].size();
        for (int i = 0; i < n; i++)
        {
            int p1 = 0;
            int p2 = m - 1;
            while (p1 <= p2)
            {
                int temp = image[i][p1];
                image[i][p1] = 1 - image[i][p2];
                image[i][p2] = 1 - temp;
                p1++;
                p2--;
            }
        }
        return image;
    }
};

int main()
{
    return 0;
}