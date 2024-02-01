class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        k %= n # Handle cases where k is larger than n

        nums[:] = nums[-k:] + nums[:-k] # this to shift right for left it will be nums[k:] + nums[:k]
