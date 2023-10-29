class Solution(object):
    def getConcatenation(self, nums: list) -> list:
        return nums * 2


print(Solution().getConcatenation([1, 2, 3]))
print(Solution().getConcatenation([1, 2, 3, 3, 2]))
