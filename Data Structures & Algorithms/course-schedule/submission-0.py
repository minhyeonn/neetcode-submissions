class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hash = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            hash[crs].append(pre)
        
        visited = set()

        def dfs(crs):
            if crs in visited:
                return False
            if hash[crs] == []:
                return True
            visited.add(crs)

            for pre in hash[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            hash[crs] = []
            return True


        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True