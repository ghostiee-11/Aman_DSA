class Solution {
public:
    bool isPalindrome(int x) {
        long long rev = 0;
        int num = x;

        while (x>0) {
            int lastdigit = x%10;
            rev = (rev*10) + lastdigit;
            x = x/10;     
        }
        if (rev == num){
            return true;
        } else{
            return false;
        } 
        
    }
};