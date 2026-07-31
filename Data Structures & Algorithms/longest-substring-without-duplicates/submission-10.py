class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        res = 1
        seen = set()
        seen.add(s[0])
        l = 0
        r = 1
        while r<len(s):
            if s[r] not in seen:
                res = max(res, r-l+1)
            else:
                while s[r] in seen:
                    seen.remove(s[l])
                    l+=1
            seen.add(s[r])
            r+=1

        return res
