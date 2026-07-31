class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> anagramMap;
        for (string word : strs) {
        string key = word;
        sort(key.begin(), key.end()); // Sort characters to create key
        anagramMap[key].push_back(word); // Group by sorted key
    }
    
        vector<vector<string>> result;
        for (auto& pair : anagramMap) {
        result.push_back(pair.second);
    }
    return result;
    }
};
