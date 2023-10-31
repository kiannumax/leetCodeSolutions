class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = min(strs)

        for char in strs:
            for i in range(0, len(prefix)):
                if prefix[i] != char[i]:
                    prefix = prefix[:i]
                    break

        return prefix

print(Solution().longestCommonPrefix(["cir","car"]))
print(Solution().longestCommonPrefix(["flower","flow","flight"]))
print(Solution().longestCommonPrefix(["dog","racecar","car"]))
