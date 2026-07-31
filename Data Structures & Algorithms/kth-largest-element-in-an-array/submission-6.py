class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums)-k

        def quickSelect(l,r):
            pivot = nums[r]
            p = l
            for i in range(l,r): #we put all the elements less than the pivot on the left and greater than the element on the right
                if nums[i]<=pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p+=1
            nums[p], nums[r]= pivot, nums[p]

            if p>k: #since p is ALWAYS gonna be at the correct index, we check if p is equal to k, and if it is, we found our answer
            #if not, we recursively check the left or right half of the pivot to find k
                return quickSelect(l,p-1)
            elif p<k:
                return quickSelect(p+1,r)
            else:
                return nums[p]
        return quickSelect(0,len(nums)-1)