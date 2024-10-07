def string_bits(str):
  newstr = ''
  for i in range(len(str)):
    if (i % 2 == 0):
      newstr += str[i:i+1]
  return newstr