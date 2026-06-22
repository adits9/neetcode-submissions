class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        val = sorted(set(nums)) #sort the nums and delete duplicates
        long = 0 #longest length counter
        localLen = 0 #local length counter
        v = val[0] #start with the min to compare all the contents of val
        print(val)
        for i in val: #go through val
            if v == i: #check if v counter is the same as the contents of val
                localLen += 1 #if yes then increment local length calculator variable
                print(localLen)
                v += 1 #increment the v to compare to
            elif v != i: #if not then
                if localLen > long: #primarily check if the local length is the same as the longest
                    long = localLen #if yes then replace
                localLen = 1
                v = i + 1
        if localLen > long: #primarily check if the local length is the same as the longest
            long = localLen #if yes then replace
        return long