class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       
        dict = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char)-ord('a')]+=1
            dict[tuple(count)].append(s)

        res = []
        for key in dict:
            res.append(dict[key])
        return res





        

        
        