def sloveit(index):
    if index == 0:
        return
    print(index, end = " ")
    sloveit(index -1)
n = int(input())
sloveit(n)
