import sys 

def add():
  f=open('data_base','r')
  temp=f.readlines() 
  f.close()
  print('enter contact name:')
  name = input()
  if name =='':
    print('No value.....')  
    return 0
  else : 
    for line in temp:
      if name in line : 
        print('Already exist.....')  
        return 0        
  
  print('enter contact telephone number:')
  number = input()
  if number =='':
    print('No value.....')
    return 0
  else:      
    for line in temp:
      if number in line: 
        print('Already exist.....')
        return 0
      
  print('enter contact mail:')
  mail = input()
  if mail =='':
    mail = 'N/A'
  else:  
    for line in temp:
      if mail in line : 
        print('Already exist.....') 
        return 0        
      
  f=open('data_base','a+')
  f.write('name: '+name+'\t\t'+'number: '+number+'\t\t'+'mail: '+mail+'\n') 
  f.close()
  return 0
def remove():
  flag =1
  print('enter contact name:')
  name = input()
  f=open('data_base','r')
  temp=f.readlines()
  f.close()  
  for line in temp:
    if name in line :
      flag=1     
    else: 
      flag=0 
  if flag ==0 :    
    print('Not exist .....')
    return 0  
     
  f=open('data_base','w')
  for line in temp:
    if name not in line:
      f.write(line)
  f.close()      
  return 0

def display():
  f=open('data_base','r')
  temp=f.readlines() 
  for line in temp :
    print(line) 
  f.close()
  return 0
  
def main():
  if str(sys.argv[1])=='add': 
    add()
  elif (sys.argv[1])=='remove':
    remove()
  elif (sys.argv[1])=='disp':
    display()    
  else:
    print('invalid operation ......\nplease enter add or remove or disp...\n')

if __name__ == '__main__':
  main()
