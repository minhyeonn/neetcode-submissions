class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> result;
        vector<int> to_be_multiplied;
        for(int i = 0;i<nums.size();++i){
            for(int j=0;j<nums.size();++j){
                if(j!=i){
                    to_be_multiplied.push_back(nums[j]);
                }
                else{
                    continue;
                }
            }
            int product = 1;
            for(int k = 0;k<to_be_multiplied.size();++k){
                product *= to_be_multiplied[k];
            }
            result.push_back(product);
            to_be_multiplied.clear();
        }
        return result;
    }
};
