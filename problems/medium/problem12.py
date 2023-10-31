class Solution:
    def intToRoman(self, num: int) -> str:
        output = ""
        romans = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400,
                  'C': 100, 'XC': 90, 'L': 50, 'XL': 40, 'X': 10,
                  'IX': 9, 'V': 5, 'IV': 4, 'I': 1}

        for key, value in romans.items():
            output += key * (num // value)
            num    -= value * (num // value)

        return output


print(Solution().intToRoman(1450))
print(Solution().intToRoman(864))
print(Solution().intToRoman(1242))

