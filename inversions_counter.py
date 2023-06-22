
def merge(sorted_first, sorted_second):
    new_array = []
    i, j = 0, 0
    swaps = 0
    while i <= len(sorted_first)-1 or j <= len(sorted_second)-1:
        if i == len(sorted_first):
            new_array.append(sorted_second[j])
            j += 1
        elif j == len(sorted_second):
            new_array.append(sorted_first[i])
            i += 1
        elif sorted_first[i] <= sorted_second[j]:
            new_array.append(sorted_first[i])
            i += 1
        else:
            new_array.append(sorted_second[j])
            j += 1
            swaps += (len(sorted_first) - i)
    return new_array, swaps


def mergesort(arr):
    if len(arr) <= 1:
        return arr, 0
    p = len(arr) // 2
    sorted_first, sw1 = mergesort(arr[:p])
    sorted_second, sw2 = mergesort(arr[p:])
    merged, sw3 = merge(sorted_first, sorted_second)
    return merged, sw1+sw2+sw3


arr1 = [5, 2, 6, 3, -1, 4, 0, 9]
swaps1 = 14

arr2 = [4, 3, 2, 1]
swaps2 = 6

print(mergesort(arr1))
print(mergesort(arr2))

