def sum13(nums):
  unlucky = False
  sum = 0
  for i in nums:
    if (i == 13):
      unlucky = True
    else:
      if (unlucky == True):
        unlucky = False
      else:
        sum += i
  return sum
