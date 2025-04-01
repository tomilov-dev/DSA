class Solution {
public:
    int findCenter(vector<vector<int>>& edges) {
        int n = edges.size();
        int f = edges[0][0];
        int s = edges[0][1];
        for (int i=1;i<n;i++) {
            for (int j=0;j<2;j++) {
                if (edges[i][j] == f) {
                    return f;
                }
            }
        }
        return s;
    }

    int findCenter(vector<vector<int>>& edges) {
        if (edges[0][0] === edges[1][0] || edges[0][0] === edges[1][1]) {
            return edges[0][0];
        }
        return edges[0][1];
    }
};