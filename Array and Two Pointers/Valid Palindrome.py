text = "madam"

def valid_palindrome(text):
    left = 0
    right = len(text)-1
    while left < right:
        if text[left] == text[right]:
            left += 1
            right -= 1
        else:
            return False
    return True


print(valid_palindrome("abba"))      # True
print(valid_palindrome("racecar"))   # True
print(valid_palindrome("hello"))     # False
print(valid_palindrome("abc"))       # False
print(valid_palindrome("a"))         # True
print(valid_palindrome(""))          # True