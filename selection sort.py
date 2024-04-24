def selection_sort(arr,size):
    n=len(arr)
    if n<=1:
        return
    for i in range ( size ):   
         key = i
         for j in range( i +1 , size ):
             if arr[j]<key:
                 key=j
         (arr[i],arr[key] )= (arr[key],arr[i])
if __name__=="__main__":
    arr=[-2, 45, 0, 11, -9, 88, -97, -202, 747]
    size=len(arr)
    selection_sort(arr,size)
    print(arr)
