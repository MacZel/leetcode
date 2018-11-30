class Solution {
public:
    vector<int> diStringMatch(string S) {
        vector<int> out_list;
        int low = 0;
        int high = S.size();
        for (int char_i=0; char_i<S.size(); char_i++) {
            if (S[char_i] == 'I') {
                out_list.push_back(low);
                low++;
            }
            else if (S[char_i] == 'D') {
                out_list.push_back(high);
                high--;
            }
        }
        out_list.push_back(low);
        return out_list;
    };
};