def last2(str):
  if len(str) < 2:
    return 0
  substr = str[len(str)-2:]
  counter = 0
  for i in range(len(str)-2):
    if (str[i:i+2] == substr):
      counter+=1
  return counter