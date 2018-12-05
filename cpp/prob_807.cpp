class Solution {
public:
    int maxIncreaseKeepingSkyline(vector<vector<int>>& grid) {
        int N = grid.size();
        vector <int> maxRows(N, 0);
        vector <int> maxCols(N, 0);
        
        for (int i=0; i<N; i++) {
            for (int j=0; j<N; j++) {
                if (grid[i][j] > maxRows[i]) {
                    maxRows[i] = grid[i][j];
                };
                if (grid[j][i] > maxCols[i]) {
                    maxCols[i] = grid[j][i];
                };
            };
        };
        
        int height_diff = 0;
        for (int i=0; i<N; i++) {
            for (int j=0; j<N; j++) {
                int max_height = min(maxRows[i], maxCols[j]);
                int curr_building_height = grid[i][j];
                if (curr_building_height < max_height) {
                    height_diff += max_height - curr_building_height;
                }  
            };
        };
        return height_diff;
    };
};