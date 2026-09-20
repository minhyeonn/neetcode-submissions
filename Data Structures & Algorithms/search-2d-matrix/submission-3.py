class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        top = 0
        bot = len(matrix)-1

        while top<=bot:
            mid = (top + bot)//2
            if matrix[mid][0]<=target<=matrix[mid][-1]:
                l = 0
                r = len(matrix[0])-1
                while l<=r:
                    m = (l+r)//2
                    if matrix[mid][m]==target:
                        return True
                    elif matrix[mid][m]<target:
                        l = m+1
                    else:
                        r = m-1
                return False
            elif target>matrix[mid][-1]:
                top = mid+1
            else:
                bot = mid-1
        return False
                
