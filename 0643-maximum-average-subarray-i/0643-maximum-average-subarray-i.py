class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current_sum = sum(nums[:k])
        best_sum = current_sum

        for right in range(k, len(nums)):
            outgoing = nums[right - k]
            incoming = nums[right]

            current_sum = current_sum - outgoing + incoming

            best_sum = max(best_sum, current_sum)
        return best_sum / k
        
            
        