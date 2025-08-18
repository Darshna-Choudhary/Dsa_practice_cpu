# Input:
# a = [1, 2, 3, 2, 1]
# b = [3, 2, 2, 3, 3, 2]

# Output:
# union of sets: {1, 2, 3}
# intersection of sets: {2, 3}

def findUnion(a, b):
        a = set(a)
        b = set(b)
        union = a.union(b)
        intersection = a.intersection(b)
        print("union of sets:",union)
        print("intersection of sets:",intersection)

findUnion(a, b)
