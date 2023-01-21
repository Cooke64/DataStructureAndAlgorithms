from collections import defaultdict
from functools import reduce


class Solution(object):
    def differenceOfSum(self, nums):
        return sum(nums) - sum((map(int, ''.join(map(str, nums)))))

    def shuffle(self, nums, n):
        arr1 = nums[:n]
        arr2 = nums[n:]
        res = []
        for i in zip(arr1, arr2):
            res.extend(i)
        return res

    def runningSum(self, nums):
        return [sum(nums[:i + 1]) for i in range(len(nums))]

    def running_sum_inplace(self, nums):
        for i in range(len(nums) - 1):
            nums[i + 1] += nums[i]
        return nums

    def numIdenticalPairs(self, nums):
        """
        O(N**2)
        """
        c = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] == nums[j] and i < j:
                    c += 1
        return c

    def numIdenticalPairs_2(self, nums):
        """
        O(N)
        """
        repeat = defaultdict(int)
        num = 0
        for num in nums:
            num += repeat[num]
            repeat[num] += 1
        return num

    def kidsWithCandies(self, candies, extraCandies):
        max_c = max(candies)
        return [i + extraCandies >= max_c for i in candies]

    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return [sorted(nums).index(i) for i in nums]

    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(0, len(nums), 2):
            res.extend([nums[i + 1]] * nums[i])
        return res

    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(len(nums)):
            res.insert(index[i], nums[i])
        return res[:len(nums)]

    def createTargetArray_2(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        arr = []
        for n, i in zip(nums, index):
            arr[i:i] = [n]
        return arr

    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        res = [0] * len(s)
        for i in range(len(indices)):
            res[indices[i]] = s[i]
        return ''.join(res)

    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        d = {
            'type': 0,
            'color': 1,
            'name': 2
        }
        s = d[ruleKey]
        return len(list(i for i in items if i[s] == ruleValue))

    def arithmeticTriplets(self, nums, diff) -> int:

        return sum(1 for i in range(len(nums)) if
                   nums[i] + diff in nums and nums[i] + 2 * diff in nums
                   )

    def defangIPaddr(self, address: str):
        """
        :type address: str
        :rtype: str
        """
        address.replace('.', '[.]')

    def interpret(self, command: str):
        """
        :type command: str
        :rtype: str
        """
        return command.replace('()', 'o').replace('(', '').replace(')', '')

    def minimumSum(self, num: int) -> int:
        """
        sorted(int(s[0]+s[2])+int(s[1]+s[3])) всегда дает минимальную
         последовательность элементов
        """
        d = sorted(str(num))
        return int(d[0] + d[2]) + int(d[1] + d[3])


    def deleteGreatestValue(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        return sum(map(max, zip(*map(sorted, grid))))

    def sortPeople(self, names, heights):
        return [name for _, name in sorted(zip(heights, names), reverse=True)]


s = Solution()

print(type(s))
