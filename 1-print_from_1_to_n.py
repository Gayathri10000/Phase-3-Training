def ispossible(index,n):
  if index >n:
    return
    
  print(index, end = " ")
  ispossible(index+1,n)
  
n = int(input())
ispossible(1,n)
