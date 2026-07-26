class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #revisited btw 
        #optimal solution - hash set 
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False 