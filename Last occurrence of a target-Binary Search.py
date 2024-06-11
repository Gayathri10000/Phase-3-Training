# last occurance of the value using the binary search
def findLastoccurance(nums,target):
  n = len(nums)
  left,right = 0,n-1
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

nums = [1,1,3,4,8,8,8]
print(findLastoccurance(nums,8))
