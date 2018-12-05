class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int target_index = 0;
        for (int i=0; i<nums.size(); i++) {
            if (target > nums[i]) {
                target_index++;
            };
        };
        return target_index;
    };
};