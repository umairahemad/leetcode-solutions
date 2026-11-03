class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(1 + i, len(nums)):
                if nums[i] == target - nums[j]:
                    return[i, j]
        