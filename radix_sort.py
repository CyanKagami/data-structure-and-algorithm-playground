import random
 
def radix_sort(arr):
    most = len(str(max(arr)))
    for i in range(most):
        counting_sort(arr,10**i)

def counting_sort(arr,exp):
    count = [0,0,0,0,0,0,0,0,0,0]
    for i in arr:
        n = (i//exp)%10
        count[n]+=1
    index = 0
    for i,val in enumerate(count):
        if val:
            count[i] = index
            index+=val
    for i in arr.copy():
        arr[count[(i//exp)%10]] = i
        count[(i//exp)%10]+=1

def main():
    rand_list=[]
    n = 100
    for _ in range(n):
        rand_list.append(random.randint(1,10000))
    radix_sort(rand_list)
    print(rand_list)

main()