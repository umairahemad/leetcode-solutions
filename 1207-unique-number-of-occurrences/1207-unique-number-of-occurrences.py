class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq_map = {}
        for num in arr:
            freq_map[num] = freq_map.get(num, 0) + 1

        seen_frequencies = set()
        for count in freq_map.values():
            if count in seen_frequencies:
                return False 
            seen_frequencies.add(count)
        return True
        