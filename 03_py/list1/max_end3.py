def max_end3(nums):
    higher = max(nums[0], nums[len(nums)-1])
    for i in range(len(nums)):
        nums[i] = higher
    return nums
