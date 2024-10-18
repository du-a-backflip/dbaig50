def centered_average(nums):
  sum = 0
  nums.remove(min(nums))
  nums.remove(max(nums))
  for i in nums:
    sum += i
  return sum/len(nums)