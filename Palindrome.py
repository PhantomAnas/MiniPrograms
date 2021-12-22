

def isPalindrome(s):
    if s == s[::-1]:
        return True
    return False

s = input('Enter String: ')
print(isPalindrome(s))