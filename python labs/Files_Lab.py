import sys,os

#Write a function named countEndWrd that takes 2 arguments filename and word.
#Count how many times the given word appears at the end of a line, 
#Then append the following string to the passed file : 
#'The word => '+"'"+word+"'"+' appears => '+count+' times' .
'''
Write your function Here
'''

def countEndWrd(filename,word):
  count=0
  ss=0
  f=open(filename,'r')
  temp=f.readlines()
  f.seek(0)
  for line in temp:
    if line.endswith(str(word+'\n')):
      count=count+1
  f.seek(0)    
  f.close()
  f=open(filename,'a+')  
  ss='The word => '+"'"+word+"'"+' appears => '+str(count)+' times'
  f.write(ss)
  f.seek(0)
  f.close()  

  
#Write a function named copyWrdToFile that takes 2 arguments source_file and word.
#It should copy all lines that contain the passed word from the file source_file 
#to a new file named 'new_file.txt'. 
'''
Write your function Here
'''
def copyWrdToFile(source_file,word):
  f1=open(source_file,'r')
  f2=open('new_file.txt','a+') 
  temp=f1.readlines()
  f1.seek(0)
  f2.seek(0)
  for line in temp:
    if word in line:
      f2.write(line)
    
  f1.seek(0)
  f1.close()
  f2.seek(0)
  f2.close()




#Provided function to test your solution.  
def testAll():
  f=open('countEndWrd.txt','r')
  temp_list=f.readlines()
  if temp_list[len(temp_list)-1] == "The word => 'END' appears => 2 times":
    #print(temp_list[len(temp_list)-1])
    print ('countEndWrd=OK')
  else:
    #print(temp_list[len(temp_list)-1])
    print ('countEndWrd=NOK')
  f.close()
  
  if os.path.exists('new_file.txt'):
    f=open('new_file.txt','r')
    temp_list=f.readlines()
    f.close()
    if len(temp_list) == 3:
      if temp_list[0] =='A person can live without food for about a'\
      +' month, but only about a week without water.\n' and temp_list[1]\
      == 'Gopher snakes in Arizona are not poisonous, but when frightened'\
      +' they may hiss and shake their tails like rattlesnakes.\n' and temp_list[2]\
      == 'Cats sleep up to eighteen hours a day, but never'\
      +' quite as deep as humans. Instead, they fall asleep quickly and '\
      +'wake up intermittently to check to see if their environment is still safe.\n': 
        print ('copyWrdToFile=OK')
      else:
        print ('copyWrdToFile=NOK')
    else:
      print ('copyWrdToFile=NOK')
  else:
    print ('copyWrdToFile=NOK')

def main():
  countEndWrd('countEndWrd.txt','END')
  copyWrdToFile('copyWrdToFile.txt','but')
  testAll()

if __name__ == '__main__':
  main()  

  