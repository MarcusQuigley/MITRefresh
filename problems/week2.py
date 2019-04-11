#problem set 1

def counting_vowels(s):
  if (s is None):
    return -1
  num_vowels = 0
  for c in s.lower():
    if c in 'aeiou':# == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
      num_vowels+=1
    
  return num_vowels

def counting_bobs(s):
  if (s is None): return -1
  num_bobs = 0
  s = s.lower()
  for i in range(1,len(s)-1):
    if (s[i-1:i+2] == 'bob'):
      num_bobs+=1
  return num_bobs

def item_order(order):
  if(order is None or len(order) == 0): return ""

  nums_salad = count_word(order,'salad')
  nums_water = count_word(order,'water')
  nums_hamburger = count_word(order,'hamburger')
  return f'salad:{nums_salad} hamburger:{nums_hamburger} water:{nums_water}'

def count_word(sentence, word):
  if(word is None or len(word) == 0): return -1
  word = word.lower()
  word_count = 0
  for i in range(1,len(sentence)-1):
    if (sentence[i-1:i+len(word)-1] == word):
      word_count+=1
  return word_count

