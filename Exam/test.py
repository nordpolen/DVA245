def is_palindrome(word):
    return word == word[::-1].lower()

print(is_palindrome("racecar")) # True
print(is_palindrome("banan")) 