class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        result = []
        
        for k, trim in queries:
            # Trim each number to rightmost 'trim' digits
            trimmed = [(num[-trim:], i) for i, num in enumerate(nums)]
            # Sort by trimmed value (string comparison works for equal length)
            trimmed.sort(key=lambda x: (x[0], x[1]))
            # Get k-th smallest (1-indexed)
            result.append(trimmed[k-1][1])
        
        return result