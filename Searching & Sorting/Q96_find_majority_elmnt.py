# A majority element in an array is an element that appears strictly more than arr.size()/2 times in the array.

# Input: arr[] = [1, 1, 2, 1, 3, 5, 1]
# Output: 1

from collections import Counter
def majorityElement(arr):
    freq = Counter(arr)
    for k, v in freq.items():
        if v > (len(arr))//2:
            return k
    return -1

print(majorityElement(arr))
