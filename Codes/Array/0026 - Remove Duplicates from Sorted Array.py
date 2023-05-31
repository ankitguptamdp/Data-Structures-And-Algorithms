class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = 0
        for index in range(len(nums)):
            if nums[index] != nums[prev]:
                prev += 1
                nums[prev] = nums[index]

        return prev + 1