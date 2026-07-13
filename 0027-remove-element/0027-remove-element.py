class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #revisited 
        j = 0 
        for x in nums:
            if x != val:
                nums[j] = x
                j += 1
        return j