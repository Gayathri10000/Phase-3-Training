def sloveit(index,nums,n):
    if index == n:
        return 100000000000
    nextele = sloveit(index+1,nums,n)
    return min(nums[index],nextele)
    # if nums[index] < nextele:
    #     return nums[index]
    # return nextele
    
nums = [1,2,34,5,667]
res = sloveit(0,nums,len(nums))
print(res)
