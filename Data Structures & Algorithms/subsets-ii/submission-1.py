class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []

        def backtrack(i):
            if i == len(nums):
                v = sorted(subset.copy())
                if v not in result:
                    result.append(v)
                return
            
            subset.append(nums[i])
            backtrack(i + 1)

            subset.pop()
            backtrack(i + 1)

        backtrack(0)

        
        return result