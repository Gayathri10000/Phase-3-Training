def palindrome_or_not(word, left, right):
    if left >= right:
        return True
    elif word[left] != word[right]:
        return False
    return palindrome_or_not(word, left + 1, right - 1)

word = 'madama'
res = palindrome_or_not(word, 0, len(word) - 1)
if res:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
