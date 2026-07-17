class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #revisited
        #optimal solution 
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1
            if count[num] > len(nums) // 2:
                return num 
