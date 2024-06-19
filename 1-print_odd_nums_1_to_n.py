def sloveit(index,n):
    if index >n:
        return 
    print(index, end = " ")
    sloveit(index +2,n)
n = int(input())
sloveit(1,n)
