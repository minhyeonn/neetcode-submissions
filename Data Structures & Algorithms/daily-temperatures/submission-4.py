class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []

        res = [0] * len(temperatures)


        for i, n in enumerate(temperatures):
            while stack and n>stack[-1][0]:
                res[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
            stack.append((n, i))

        return res

