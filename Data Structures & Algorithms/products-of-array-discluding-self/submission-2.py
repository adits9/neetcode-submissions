class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #creating 3 arrays, final, prefix, and suffix
        #each index represents the product of the past or subsequent numbers in prefix and suffix arrays
        #then in final array multiply the same index of prefix and suffix for that particular final result
        n = len(nums)
        res = [0] * n
        pref = [0] * n
        suff = [0] * n

        pref[0] = suff[n - 1] = 1
        for i in range(1, n):
            pref[i] = nums[i - 1] * pref[i - 1]
        for i in range(n - 2, -1, -1):
            suff[i] = nums[i + 1] * suff[i + 1]
        for i in range(n):
            res[i] = pref[i] * suff[i]
        return res