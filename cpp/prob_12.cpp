class Solution {
public:
    string intToRoman(int num) {        
        vector <vector <char>> int2roman = {
            {'I', 'V'},
            {'X', 'L'},
            {'C', 'D'},
            {'M'}
        };
        string ans;
        for (int i=0; i<4; i++) {
            int digit = num % 10;
            num /= 10;
            stringstream pre;
            
            if (digit < 4) {
                pre << string(digit, int2roman[i][0]);
            }
            else if (digit == 4) {
                pre << int2roman[i][0] << int2roman[i][1] ;
            }
            else if (digit < 9) {
                pre << int2roman[i][1] << string((digit % 5), int2roman[i][0]);
            }
            else {
                pre << int2roman[i][0] << int2roman[i+1][0];
            }
            ans = pre.str() + ans;
        }
        return ans;
    };
};