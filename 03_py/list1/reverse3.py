def reverse3(nums):
    first = nums[0]
    for i in range(len(nums)/2):
        first = nums[i]
        nums[i] = nums[len(nums)-1-i]
        nums[len(nums)-1-i] = first
    return nums
