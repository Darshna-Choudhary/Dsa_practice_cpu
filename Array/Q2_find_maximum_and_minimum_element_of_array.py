# Input: arr = [3, 5, 4, 1, 9]
# Output:
# min element : 1
# max element : 9

def find_min(arr):
    min_elmnt = 100000
    for i in range(len(arr)):
        if arr[i] < min_elmnt:
            min_elmnt = arr[i]
    return min_elmnt


def find_max(arr):
    max_elmnt = -100000
    for i in range(len(arr)):
        if arr[i] > max_elmnt:
            max_elmnt = arr[i]
    return max_elmnt


print("min element :",find_min(arr))
print("max element :",find_max(arr))
