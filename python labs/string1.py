#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Basic string exercises
# Fill in the code for the functions below. main() is already set up
# to call the functions with a few different inputs,
# printing 'OK' when each function is correct.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code.
# It's ok if you do not complete all the functions, and there
# are some additional functions to try in string2.py.


# A. donuts
# Given an int count of a number of donuts, return a string
# of the form 'Number of donuts: <count>', where <count> is the number
# passed in. However, if the count is between or equal 15 to 100, then use the word 'many'
# instead of the actual count, elif the count is more 100, 
# then use the words 'too much donuts' instead of the actual count.
# So donuts(5) returns 'Number of donuts: 5'
# and donuts(23) returns 'Number of donuts: many'
# and donuts(101) returns 'Number of donuts: too much donuts'
def donuts(count):
  # +++your code here+++
  if count>100:
    return "Number of donuts: too much donuts"
  elif 15<=count<=100:
    return "Number of donuts: many"
  elif count<=5:
    return str("Number of donuts: "+str(count))  
  else:
    None  
  return

# B. both_ends
# Given a string s, return a string made of the first 2
# and the last 2 chars of the original string,
# so 'spring' yields 'spng'. However, if the string length
# is less than 2, return the string "invalid input".
def both_ends(s):
  # +++your code here+++
  if len(s)<2:
    return  "invalid input"
  else :
    s = s[0]+s[1]+s[-2]+s[-1]
    return s   
  
  return


# C. fix_start
# Given a string s, return a string
# where all occurences of its first char have
# been changed to the symbol written inside the input argument filler, except do not change
# the first char itself.
# e.g. 'babble' yields 'ba!!le' if filler is = !
# Assume that the string is length 1 or more.
# Hint: s.replace(stra, strb) returns a version of string s
# where all instances of stra have been replaced by strb.

def fix_start(s,filler):
  # +++your code here+++
  for i in range(len(s)):
    if s[i] == s[0]:
      return s[0] + s[1:].replace(s[i], filler)
  return s
    
    
    
    
    
# D. MixUp
# Given strings a and b, return a single string with a and b separated
# by a - '<a>-<b>', except swap the first 2 chars of each string.
# e.g.
#   'mix', pod' -> 'pox-mid'
#   'dog', 'dinner' -> 'dig-donner'
# Assume a and b are length 2 or more.
def mix_up(a, b):
  # +++your code here+++
  swapa = b[:2]
  swapb = a[:2]
  return swapa + a[2:] + "-" + swapb + b[2:]



# Provided simple test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print ('%s got: %s expected: %s' %(prefix, repr(got), repr(expected)))


# Provided main() calls the above functions with interesting inputs,
# using test() to check if each result is correct or not.
def main():
  print ('donuts')
  # Each line calls donuts, compares its result to the expected for that call.
  test(donuts(4), 'Number of donuts: 4')
  test(donuts(15), 'Number of donuts: many')
  test(donuts(100), 'Number of donuts: many')
  test(donuts(110), 'Number of donuts: too much donuts')

  print()
  print ('both_ends')
  test(both_ends('spring'), 'spng')
  test(both_ends('Hello'), 'Helo')
  test(both_ends('a'), 'invalid input')
  test(both_ends('xyz'), 'xyyz')

  
  print ()
  print ('fix_start')
  test(fix_start('babble','!'), 'ba!!le')
  test(fix_start('aardvark','*'), 'a*rdv*rk')
  test(fix_start('google','' ), 'goole')
  test(fix_start('donut','#'), 'donut')

  print ()
  print ('mix_up')
  test(mix_up('mix', 'pod'), 'pox-mid')
  test(mix_up('dog', 'dinner'), 'dig-donner')
  test(mix_up('gnash', 'sport'), 'spash-gnort')
  test(mix_up('pezzy', 'firm'), 'fizzy-perm')


# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main()

