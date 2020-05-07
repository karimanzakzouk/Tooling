arr=[5,2,3,4,1,8,2,7,0,5,1,9]

def sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)) :
            if arr[i] < arr[j]:
                t = arr[i]
                arr[i]= arr[j]
                arr[j]= t
    
    return arr 
   
print(sort(arr))            
            
        