class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)

        store_index = 2 

        for check_index in range (2, len(nums)):
            if nums[check_index] != nums[store_index - 2]:
                nums[store_index] = nums[check_index]
                store_index += 1 

        return store_index
             




            