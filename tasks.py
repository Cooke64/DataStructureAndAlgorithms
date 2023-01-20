class Solution(object):
    def differenceOfSum(self, nums):
        return sum(nums) - sum((map(int, ''.join(map(str, nums)))))


s = Solution()
print(s.differenceOfSum([1, 15, 6, 3]))
