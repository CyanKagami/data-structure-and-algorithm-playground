def counting_sort(arr):
    count = [0,0,0,0,0,0,0,0,0,0]
    for i in arr:
        count[i]+=1
    index = 0
    for i,val in enumerate(count):
        if val:
            count[i] = index
            index+=val
    for i in arr.copy():
        arr[count[i]] = i
        count[i]+=1

arr = [5,7,4,1,3,3]
counting_sort(arr)
print(arr)