class Solution {
public:
    int peakIndexInMountainArray(vector<int>& A) {
        int curr_max = 0;
        int curr_peak = 0;
        for (int i=0; i<A.size(); i++) {
            if (A[i] > curr_max) {
                curr_max = A[i];
                curr_peak = i;
            };
        };
        return curr_peak;
    };
};