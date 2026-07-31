class Solution {
public:

    string encode(vector<string>& strs) {
        string single = "";
        for(int i=0;i<strs.size();++i){
            single += to_string(strs[i].size()) + "#" + strs[i];
        }
        return single;
    }

    vector<string> decode(string s) {
        vector<string> result;
            int i=0;
        
        while(i<s.length()){
            int j = i;
        while (s[j] != '#') {
                ++j;
        }
        int len = stoi(s.substr(i, j-i));
        string word = s.substr(j+1, len);
        result.push_back(word);
        i=j+len+1;
        }
        return result;
    }
    
};
