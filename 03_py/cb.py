#Dua Baig
#SoftDev
#K03 -- Reviewing python lists
#2024-09-12
#time spent: .5

def sleep_in(weekday, vacation):
  return not weekday or vacation

def monkey_trouble(a_smile, b_smile):
  return a_smile == b_smile

def sum_double(a, b):
  if (a == b):
    return (a+b) * 2
  else:
    return a+b

def diff21(n):
  if (n <= 21):
    return abs(n-21)
  else:
    return 2 * abs(n-21)

def parrot_trouble(talking, hour):
  return talking and (hour < 7 or hour > 20)

def makes10(a, b):
  return (a == 10 or b == 10) or a + b == 10

def near_hundred(n):
  return abs(n -100) <= 10 or abs(n-200) <= 10

def pos_neg(a, b, negative):
  if negative:
    return a < 0 and b < 0 
  else:
    return (a < 0 and b > 0) or (b < 0 and a > 0)

def not_string(str):
  if (len(str) >= 3):
    if str[0:3] != "not":
      return "not " + str
    else:
      return str
  else: 
    return "not " + str

def missing_char(str, n):
  return str[0:n] + str[n+1:]

def front_back(str):
  if (len(str) >= 2):
    return str[len(str)-1:] + str[1:len(str)-1] + str[0:1]
  else:
    return str

def front3(str):
  if (len(str) >= 3):
    return str[0:3]*3
  else:
    return str * 3


  
