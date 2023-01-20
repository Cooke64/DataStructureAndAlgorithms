def search_insert(nums: list[int], target: int) -> int:
    """Поиск в упорядоченном массиве по не убыванию индекса числа."""
    if target in nums:
        return nums.index(target)
    for i in range(1, len(nums)):
        if nums[i - 1] < target < nums[i]:
            return i
    return 0 if min(nums) > target else len(nums)


def search_insert_bin(nums, target):
    low = 0
    high = len(nums)
    while low < high:
        middle = (high + low) // 2
        if nums[middle] == target:
            return middle
        elif nums[middle] < target:
            low = middle + 1
        else:
            high = middle
    return low
