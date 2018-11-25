class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (!nums.size()) {
            return 0;
        }
        
        int carret = 0;
        for (int i=1; i < nums.size(); i++) {
            if (nums[carret] != nums[i]) {
                carret++;
                nums[carret] = nums[i];
            }
        }
        return carret + 1;
    }
};