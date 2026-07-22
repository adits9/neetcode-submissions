class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        subset = []

        def backtrack(i):
            if i >= len(nums) or sum(subset) >= target:
                if sum(subset) == target:
                    result.append(subset.copy())
                return
                
            subset.append(nums[i])
            backtrack(i)

            subset.pop()
            backtrack(i + 1)

        backtrack(0)
        return result