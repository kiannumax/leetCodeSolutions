class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0

        num += (1000 * s.count('M')) - (200 * (s.count('CM') + s.count('CD')))
        num += (500 * s.count('D')) - (20 * (s.count('XC') + s.count('XL')))
        num += (100 * s.count('C')) - (2 * (s.count('IX') + s.count('IV')))
        num += (50 * s.count('L')) + (10 * s.count('X'))
        num += (5 * s.count('V')) + (1 * s.count('I'))

        return num

print(Solution().romanToInt("MCMXCIV"))
print(Solution().romanToInt("MDCCXXIV"))
