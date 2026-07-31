class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       res = {}

       for word in strs:
          freq = [0] * 26
          for char in word:
            freq[ord(char)-ord('a')]+=1
          if tuple(freq) in res:
            res[tuple(freq)].append(word)
          else:
            res[tuple(freq)] = [word]

       return list(res.values())

        




        

        
        