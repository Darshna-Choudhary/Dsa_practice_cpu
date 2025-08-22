# Input: nums = [1,3,4,2,2]
# Output: 2

def findDuplicate(nums):
    dct = {}
    for i in range(len(nums)):
        if nums[i] not in dct:
            dct[nums[i]] = 1
        else:
            dct[nums[i]] += 1
    for k, v in dct.items():
        if v != 1:
            return k

print(findDuplicate(nums))
