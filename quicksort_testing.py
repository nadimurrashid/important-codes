
def partition(arr,start,end):

    pivot = arr[end]
    i = start-1
    j = start

    while j < end:
        if arr[pivot] >= arr[j]:
            i = i + 1
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
        j = j+1

    arr[i+1],arr[end] = arr[end],arr[i+1]
    print(arr[end])
    return i+1

def quicksort(arr, start, end):
    if start < end:
        pivot = partition(arr, start, end)
        quicksort(arr, start, pivot - 1)
        quicksort(arr, pivot + 1, end)


a = [2, 3, 5, 1, 4]
x = quicksort(a, 0, len(a) - 1)
print(a)














