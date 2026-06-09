class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i, n in enumerate(nums):
            comp = target - n
            if comp in nums and i != nums.index(comp):
                return [min(i, nums.index(comp)), max(i, nums.index(comp))]