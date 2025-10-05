import bisect

class Solution:
    def search(self, nums, target):
        i = bisect.bisect_left(nums, target)  # first index with nums[i] >= target
        return i if i < len(nums) and nums[i] == target else -1
