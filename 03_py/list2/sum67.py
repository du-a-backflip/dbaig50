def sum67(nums):
  six = False
  sum = 0
  for i in nums:
    if (i == 6):
      six = True
    elif (i == 7 and six == True):
      six = False
    else:
      if (six != True):
        sum += i
  return sum