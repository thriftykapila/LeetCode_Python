def isPalindrome(x):
    return (True if str(x) == str(x)[::-1] else False)


print(isPalindrome(12321))
