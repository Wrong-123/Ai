
arr=[]
n=int(input("enter size of list->"))

for i in range(n):
    num=int(input("enter numbers->"))
    arr.append(num)



def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_index=i

        for j in range(i+1,n):
            if arr[j] < arr[min_index]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
        print(f"After Pass{i} sorted-> ",arr)

    return arr


sorted_arr=selection_sort(arr)
print("Sorted arr is",sorted_arr)