class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        int n = nums.size();
        vector<int> out; 

        for(int i=0; i<n; i++){
            out.push_back(nums[i]);
        }        

        for(int i=0; i<n; i++){
            out.push_back(nums[i]);
        }
        return out;
    }
};