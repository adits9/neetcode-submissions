class Solution:
    def search(self, nums: List[int], target: int) -> int:
        e = 0
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] > nums[r]:
                l = m + 1
            elif nums[m] < nums[r]:
                r = m
            else:
                e = m
                break

        def bs (l, r, target):
            while l <= r:
                m = (l + r) // 2
                
                if nums[m] > target:
                    r = m - 1
                elif nums[m] < target:
                    l = m + 1
                else:
                    return m
            return -1

        q1 = bs(0, e - 1, target)
        if q1 != -1:
            return q1
        else:
            q2 = bs (e, len(nums) - 1, target)
            return q2