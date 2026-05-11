class Solution {
public:
    vector<int> separateDigits(vector<int>& nums) {
        vector<int> result;

        for (int i = 0; i < nums.size(); i++) {
            int num = nums[i];
            vector<int> temp;

            // Extract digits
            while (num > 0) {
                temp.push_back(num % 10);
                num /= 10;
            }

            // Reverse to maintain order
            reverse(temp.begin(), temp.end());

            // Add to result
            for (int d : temp) {
                result.push_back(d);
            }
        }

        return result;
    }
};