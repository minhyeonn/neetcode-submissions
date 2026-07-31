class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if(nums.empty()){
            return 0;
        }
        vector<int> sorted_nums = nums;
        sort(sorted_nums.begin(), sorted_nums.end());
        vector<int> maxes;
        int count = 1;
        
        for(int i =1;i<sorted_nums.size();++i){
            if(sorted_nums[i-1]+1==sorted_nums[i]) {
                ++count;
            }
            else if(sorted_nums[i-1]==sorted_nums[i]){
                continue;
            }
            else{
                maxes.push_back(count);
                count = 1;
            }
            maxes.push_back(count);
        }
        int max = 1;
        for(int i = 0;i<maxes.size();++i){
            if(maxes[i]>max){
                max = maxes[i];
            }
        }
        return max;
    }



};