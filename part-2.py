# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    if len(array) == 0:
        return False
    if array[0] == query:
        return True
    return search(array[1:], query)

# is_palindrome
def is_palindrome(text):
    if len(text) <= 1:
        return True
    if text[0] == text[-1]:
        return is_palindrome(text[1:-1])
    return False


# digit_match
# I didn't pass test. Still working on it
def digit_match(num1, num2):
    if num1 == 0 and num2 == 0:
        return 1

    if num1 == 0 or num2 == 0:
        return 0

    if num1 % 10 == num2 % 10:
        return 1 + digit_match(num1 // 10, num2 // 10)
    else:
        return digit_match(num1 // 10, num2 // 10)

