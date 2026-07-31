class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(cur_list, open, close):
            if open==close==n:
                res.append("".join(cur_list))
                return
            
            
            if open<n:
                cur_list.append("(")
                backtrack(cur_list, open+1, close)
                cur_list.pop()

            if close<open:
                cur_list.append(")")
                backtrack(cur_list, open, close+1)
                cur_list.pop()

        backtrack([],0,0)
        return res