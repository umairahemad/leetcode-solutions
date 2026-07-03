class Solution:
    def reverseString(self, s: List[str]) -> None:
        #two pointer approach
        # we can also use built-in function s.reverse() but its not the optimal solution 
        left = 0
        right = len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        
        