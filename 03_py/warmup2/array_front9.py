def array_front9(nums):
  length = 4
  if len(nums) < 4:
    length = len(nums)
  for i in range(length):
    if (nums[i] == 9):
      return True
  return False