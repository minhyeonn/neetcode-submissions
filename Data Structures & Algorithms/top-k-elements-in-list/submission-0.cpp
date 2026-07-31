class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        map<int, int> ordered;
        for(int i = 0;i<nums.size();++i){
            int key = nums[i];
            ordered[key]++;
        }

            vector<int> result;
            int i =0;
        while (i < k) {
            int maxFreq = 0;
            int maxKey = 0;
        for (auto& pair : ordered) {
            if (pair.second > maxFreq) {
                maxFreq = pair.second;
                maxKey = pair.first;
        }   
        }

        result.push_back(maxKey);
        ordered.erase(maxKey);
        ++i;
        }
         return result;
        }
};
