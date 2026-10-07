class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        i = 0
        while i < n and arr[i] < x:       # first index with arr[i] >= x
            i += 1

        l, r = i - 1, i                   # window is arr[l+1 : r], starts empty
        while r - l - 1 < k:
            if l < 0:                     # nothing left on the left
                r += 1
            elif r >= n:                  # nothing left on the right
                l -= 1
            elif x - arr[l] <= arr[r] - x:  # left is closer (ties go left)
                l -= 1
            else:
                r += 1

        return arr[l + 1 : r]
            

            



