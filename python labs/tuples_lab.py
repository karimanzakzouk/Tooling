#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Based on Google's Python Class
# http://code.google.com/edu/languages/google-python-class/


# sort_sum
# Given a list of non-empty tuples, return a list of tuples sorted in descending 
# order by the sum of elements in the tuple.
# e.g. [(1, 7), (1, 4), (3, 4, 5), (2, 2)] yields
# [(3, 4, 5), (1, 7), (1, 4), (2, 2)]
# Hint: use key= in sorted.
# Hint: You may need to create your own key function to calculate the sum
def summ(L):
    s=0
    for i in range(len(L)):
        s+=L[i]
    return s
    
def sort_sum(tuples): 
  # +++your code here+++
    return sorted(tuples, key=summ ,reverse=True)
  
  
  #return sorted(tuples,key=lambda x:x[0]+x[1]+x[2])
    
# even_tuple
# Given a tuple, return a tuple whose values are the even numbers of 
# the given tuple e.x. (1,2,3,4,5,6,7,8,9,10) => (2,4,6,8,10). Sort the
# output tuple in ascending order.
def evenOnly(L):
    LL=[]
    sorted(L)
    for i in L :
        if i%2 ==0 :
           LL.append(i)
    return LL 
    
def even_tuple(input_tuple):
  # +++your code here+++
  t = evenOnly(input_tuple) 
  return tuple(sorted(t))  
  
  
# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print ('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# Calls the above functions with interesting inputs.
def main():
  print ()
  print ('sort_sum')
  test(sort_sum([(0,), (3, 2), (2, 1)]),
       [(3, 2), (2, 1), (0,)])
  test(sort_sum([(5, 5), (99, 1), (7, 1)]),
       [(99, 1), (5, 5), (7, 1)])
  test(sort_sum([(1, 1), (7, 3), (8, 1), (2, 2)]),
       [(7, 3), (8, 1), (2, 2), (1, 1)])
       
  print ()
  print ('even_tuple')
  test(even_tuple((1,0,2,5,7,8,12)),
       (0,2,8,12))
  test(even_tuple((6,7,6,8,10)),
       (6,6,8,10))
  test(even_tuple((104,103,102,101,100)),
       (100,102,104))

if __name__ == '__main__':
  main()
  