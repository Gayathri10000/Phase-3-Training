
def findLastOccurrence(nums, target):
    n = len(nums)
    left, right = 0, n - 1 
    result = -1 
    while left <= right:
        mid = (left + right) // 2                   
        if nums[mid] == target:
            result = mid  
            left = mid + 1 
        elif nums[mid] > target:
            right = mid - 1 
        else:
            left = mid + 1 
    return result

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


# Total number of time the values Occurance 

def counttotaloccurance(nums,target):
    first = findFirstOccurrence(nums, target)
    if first == -1:
        return 0
    last = findLastOccurrence(nums, target)
    return last - first + 1
nums = [1, 2, 3, 4, 4, 4, 6, 7]
print(counttotaloccurance(nums,4)) # the occurance of the 4 is 3 times
