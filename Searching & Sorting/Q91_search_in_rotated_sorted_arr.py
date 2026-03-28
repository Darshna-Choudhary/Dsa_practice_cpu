# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4

def search(nums):
    st = 0
    end = len(nums) - 1
    while st <= end:
        mid = st + (end - st) // 2
        if nums[mid] == target:
            return mid
        # left part sorted
        if nums[mid] >= nums[st]:
            if target >= nums[st] and target < nums[mid]:
                end = mid - 1
            else:
                st = mid + 1
        # right part sorted
        else:
            if target > nums[mid] and target <= nums[end]:
                st = mid + 1
            else:
                end = mid - 1
    return -1

print(search(nums))
