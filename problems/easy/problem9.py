#First solution before reading that it should be done without converting to strings
class Solution1(object):
    def isPalindrome1(self, x):
        return (str(x) == str(x)[::-1])


#Actual Solution
class Solution(object):
    def isPalindrome(self, x: int) -> bool:
        if (x < 0) or (x >= 10 and x % 10 == 0):
            return False

        newX = 0
        while x > newX:
            newX = newX * 10 + x % 10
            x  //= 10

        return (newX == x) or (newX == x * 10 + newX % 10)


print(Solution().isPalindrome(121))
print(Solution().isPalindrome(1221))
print(Solution().isPalindrome(1251))
print(Solution().isPalindrome(251))
print(Solution().isPalindrome(-121))
