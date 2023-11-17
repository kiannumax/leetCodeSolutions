class Solution:
    def maxArea(self, height: list[int]) -> int:
        maxAr = left = 0
        right = len(height) - 1

        while right > left:
            if (test := min(height[left], height[right]) * (right - left)) > maxAr:
                maxAr = test

            if height[left] >= height[right]:
                right -= 1

            else:
                left += 1

        return maxAr


print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))
print(Solution().maxArea([1,1]))
