class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int n = s.length();
        vector<int> chartable(128, 0);
        int ans = 0;
        
        for (int i=0, j=0; j < n; j++) {
            i = max(chartable[int(s[j])], i);
            ans = max(ans, j-i+1);
            chartable[int(s[j])] = j+1;
        };
        
        return ans;  
    };
};
