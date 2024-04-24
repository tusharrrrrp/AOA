'''step1) get the len of the arr
   step2) for i in any range btw 1 to n arr[i] will be stored as key
          and we will take another vairable for another number and the number will be i-1
          then
          while j>=0 and key<arr[j]
               arr[j+1] will become arr[j] for shiting the element towards right we will decrement it by 1
               j-=1
                and now store that new arr[j+1] as new key
   step3) the final one '''
def insertion_sort(arr):
    n=len(arr)
    for i in range (1,n): 
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
            arr[j+1]=key

if __name__=="__main__":
    arr=[16,5,6,12,14]
    insertion_sort(arr)
    print(arr)
