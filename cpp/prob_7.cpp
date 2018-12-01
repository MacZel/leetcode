class Solution {
public:
    int reverse(int x) {
        int neg = x < 0 ? -1 : 1;
        x = abs(x);

        double ans = 0;
        while(x != 0) {
            ans = ans * 10 + x % 10;
            x = (int) (x / 10);
        };
        
        ans *= neg;
        
        double lim = pow(2, 31); // or 2147483648
        if (ans >= -lim and ans <= lim-1) {
            return ans;
        }
        else {
            return 0;
        };
    };
};