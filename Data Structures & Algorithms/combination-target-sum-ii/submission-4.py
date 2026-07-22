class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        result = []
        subset = []

        def backtrack(i):
            total = sum(subset)

            if total == target:
                result.append(subset.copy())
                return

            if i >= len(candidates) or total > target:
                return

            subset.append(candidates[i])
            backtrack(i + 1)
            subset.pop()

            while (
                i + 1 < len(candidates)
                and candidates[i] == candidates[i + 1]
            ):
                i += 1

            backtrack(i + 1)

        backtrack(0)
        return result