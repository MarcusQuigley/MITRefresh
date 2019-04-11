def oddTuples(tup):
  oddTuple = ()
  index = 0
  # for i in range(0,len(tup),2):
  #   oddList.append(tup[i])

  while index < len(tup):
    oddTuple += (tup[index],)
    index+=2
  
  return tuple(oddTuple)

def oddTuples2(tup):
  return tup[::2]


def howManyValues(dict):
  return len(dict.values())
  counter = 0
  print(dict.values())
  for i in dict.values():
    counter+=1
  
  return counter

def largestValues(dict):
  maxvalue=0
  key=''

  for key in dict:
    tempLength = len(dict[key])
    if tempLength > maxvalue:
      maxvalue = tempLength
      key = key
          
  return key

def nDigits(x):
  if x == 0: return 0
  x = abs(x)
  strx = str(x)
  if len(strx) == 1: return 1
  n = len(strx)-1
  return nDigits(int(strx[:n])) + 1
