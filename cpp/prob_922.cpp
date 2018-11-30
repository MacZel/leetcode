class Solution {
public:
    vector<int> sortArrayByParityII(vector<int>& A) {
        vector<int> even_list;
        vector<int> odd_list;
        vector<int> out_list;
        for (int i=0; i<A.size(); i++) {
            if (A[i] % 2 == 0) {
                even_list.push_back(A[i]);
            }
            else {
                odd_list.push_back(A[i]);
            };
        };
        for (int i=0; i<even_list.size(); i++) {
            out_list.insert(out_list.end(), {even_list[i], odd_list[i]});
        };
        return out_list;
    };
};