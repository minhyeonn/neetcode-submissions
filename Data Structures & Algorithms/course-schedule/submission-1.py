class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq = {i:[] for i in range(numCourses)}

        for pre in prerequisites:
            prereq[pre[0]].append(pre[1])
        

        visit = set()

        def dfs(crs):
            if crs in visit:
                return False
            if not prereq[crs]:
                return True

            visit.add(crs)

            for pre in prereq[crs]:
                if not dfs(pre):
                    return False
            visit.remove(crs)
            prereq[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True

                