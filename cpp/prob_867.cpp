class Solution {
public:
    vector<vector<int>> transpose(vector<vector<int>>& A) {
        int N_rows = A.size();
        int N_cols = A[0].size();
        # If A is a square matrix, transpose in place
        if (N_rows == N_cols) {
            for (int row_i=0; row_i<N_rows; row_i++) {
                for (int col_i=row_i+1; col_i<N_rows; col_i++) {
                    int temp = A[row_i][col_i];
                    A[row_i][col_i] = A[col_i][row_i];
                    A[col_i][row_i] = temp;
                };
            };
            return A;
        }
        # otherwise create new matrix
        else {
            vector<vector<int>> A_T;
            for (int col_i=0; col_i<N_cols; col_i++) {
                vector<int> row_T;
                for (int row_i=0; row_i<N_rows; row_i++) {
                    row_T.push_back(A[row_i][col_i]);
                };
                A_T.push_back(row_T);
            };
            return A_T;
        };
    };
};