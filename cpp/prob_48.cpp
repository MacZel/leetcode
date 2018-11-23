class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int N = matrix.size();
        
        for (int i=0; i < (int) N/2; i++) {
            
            for (int j=i; j < N-i-1; j++) {
                int copy_curr = matrix[i][j];
                int copy_next = 0;
                
                for (int k=0; k < 4; k++) {
                    int t = i;
                    i = j;
                    j = N-t-1;
                    copy_next = matrix[i][j];
                    matrix[i][j] = copy_curr;
                    copy_curr = copy_next;
                }
            }
        }
        
        return;
    }
};