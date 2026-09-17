class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""
        countT = defaultdict(int)
        window = defaultdict(int)
        
        for i in range(len(t)):
            countT[t[i]]+=1

        res = [-1,-1]
        resLen = float('inf')
        l = 0
        have = 0
        need = len(countT)

        for r in range(len(s)):
            window[s[r]]+=1

            if s[r] in countT and window[s[r]]==countT[s[r]]:
                have+=1

            while have==need:
                if r-l+1<resLen:
                    res = [l,r]
                    resLen = r-l+1
                window[s[l]]-=1
                if s[l] in countT and window[s[l]]<countT[s[l]]:
                    have-=1
                l+=1

        if resLen!=float('inf'):
            return s[res[0]:res[1]+1]
        else:
            return ""



