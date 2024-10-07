def string_splosion(str):
  newstr = ""
  for i in range(len(str)+1):
    newstr += str[0:i]
  return newstr