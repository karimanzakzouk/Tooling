#!/usr/bin/python2.4 -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Additional basic string exercises


#  testString
# Given a string, If it consists from only digits,
# return the sum of these digits as a string .
# e.x "1548" => "18"
# Elif the string consists from only alphabets,
# return the number of occurrences of each character in the string as a string.
# e.x "ABCABCABC" => "333333333" , "Google" => "222211", treat all as lower case (G=g)
# Else return the given string back
# Hint: you may need to use for and while statements 
def testString(s):
  # +++your code here+++
  counter = {}
  sum=0
  c=""
  for i in range(len(s)) :
    if s.isdigit():     
      sum+=int(s[i])
    else:
      if  any(char.isdigit() for char in s) :     
        return s  
      else :
        s= s.lower()
        for i in range(len(s)) : 
          counter[i] = s.count(s[i]) 
          c +=  str(counter[i])
          
        return  str(c)   
        
  return str(sum)
 

     
  
#  minipulateString
# Given a command and a delimiter and a target string 's', 
# If the command is 'join_str', return s joined by the given delim.
# Elif the command is 'split_str', split s using the delim and return the output.
# If the delim was an empty string use space as a default delim in both cases.
def minipulateString(command,delim,s):
  # +++your code here+++
  i=0
  s2=""
  s3=""
  if command=='join_str':
    if delim =='':
      delim = ' '    
    for i in range(len(s)) :
      s2+= s[i]
      if i!=len(s)-1: 
        s2+=delim
        
    return s2
  elif  command=='split_str':
      return s.split('-') 
  else:
    return s

  
  
#  isunicode
# Given a string 's', 
# If the string is a unicode string return "This is a unicode string".
# Else return "This is a string"
def isunicode(s):
  # +++your code here+++
  if isinstance(s, str) : #and type(s) != bytes
    return  "This is a unicode string"
  else :
    return  "This is a string"   #??????
    


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print ('%s got: %s expected: %s' %(prefix, repr(got), repr(expected)))


# main() calls the above functions with interesting inputs,
# using the above test() to check if the result is correct or not.
def main():
  print ('testString')
  test(testString('00000'), '0')
  test(testString('9876'), '30')
  test(testString('boOkkEeper'), '1222233131')
  test(testString('ITI 40'), 'ITI 40')

  print ()
  print ('minipulateString')
  test(minipulateString('join_str','~',['AB','AB','AB']), 'AB~AB~AB')
  test(minipulateString('split_str','-','ITI-40-ES'), ['ITI','40','ES'])
  test(minipulateString('join_str','',['This','tea','is','hot']), 'This tea is hot')
  

  print ()
  print ('isunicode')
  test(isunicode('test'), 'This is a string')
  test(isunicode(u'test'), 'This is a unicode string')

if __name__ == '__main__':
  main()
  