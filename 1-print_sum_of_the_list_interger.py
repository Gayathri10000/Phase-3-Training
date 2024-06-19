def sloveit(index,nums,n):
    if index ==n:
        return 0
    nextele = sloveit(index+1,nums,n)
    return nums[index] + nextele
    
nums = [1,2,34,5,67]
res = sloveit(0,nums,len(nums))
print(res)
