class Solution {
public:
    int sumOfUnique(vector<int>& nums) {
        int n = 0;

        sort(nums.begin(), nums.end());

        for(int i=0; i<nums.size(); i++) {
            bool left = (i==0 || nums[i] != nums[i-1]);
            bool right = (i==nums.size()-1 || nums[i] != nums[i+1]);

        if(left && right) {
            n += nums[i];
            }      
        }
        return n;        
    }
};