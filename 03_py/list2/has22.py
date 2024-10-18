def has22(nums):
  two = False
  for i in nums:
    if (i == 2):
      if (two):
        return True
      else:
        two = True
    else:
      if (two):
        two = False
  return False