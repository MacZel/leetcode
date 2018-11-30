class Solution {
public:
    bool isPalindrome(int x) {
        int copy_x = x;
        
        if (x < 0) {
            return false;
        }
        else {
            int reversed_x = 0;
            while (x != 0) {
                reversed_x = reversed_x *10 + x % 10;
                x = (int) (x / 10);
            };
            if (copy_x == reversed_x) {
                return true;
            }
            else {
                return false;
            };
        };
    };
};