 # First occurrence of a target using Binary Search

def findFirstOccurrence(nums, target):
    n = len(nums)
    left, right = 0, n - 1 
    result = -1 
    while left <= right:
        mid = (left + right) // 2 
        if nums[mid] == target:
            result = mid
            
            right = mid - 1
        elif nums[mid] > target:
            right = mid - 1 
        else:
            left = mid + 1 
 
    return result
nums = [1,2,2,4,4,4,5,7,8]
print(findFirstOccurrence(nums, 4))
print(findFirstOccurrence(nums, 2))
