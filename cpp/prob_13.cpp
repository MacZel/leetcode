class Solution {
public:
    int romanToInt(string s) {
        map<char, int> ROMAN2INT = {
            { 'I', 1 },
            { 'V', 5 },
            { 'X', 10 },
            { 'L', 50 },
            { 'C', 100 },
            { 'D', 500 },
            { 'M', 1000 }
        };
        
        int ans = 0;
        for (int i=0; i<s.length(); i++) {
            int sign = 1;
            if (i != s.length() - 1 && ROMAN2INT[s[i]] < ROMAN2INT[s[i+1]]) {
                sign = -1;
            };
            ans += sign * ROMAN2INT[s[i]];
        };
        return ans;
    };
};