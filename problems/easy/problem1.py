
class Solution:
    # Better for speed
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        differences = {}

        for i in range(0, len(nums)):
            if nums[i] in differences:
                return [differences[nums[i]], i]

            differences[target - nums[i]] = i

    #Better for memory
    def twoSum2(self, nums: list[int], target: int) -> list[int]:
        for i in range(0, len(nums)):
            for i2 in range(0, len(nums)):
                if nums[i] + nums[i2] == target and i != i2:
                    return [i, i2]



print(Solution().twoSum([3, 2, 4], 6))
print(Solution().twoSum([2,7,11,15], 9))
print(Solution().twoSum([3, 3, 3], 6))
