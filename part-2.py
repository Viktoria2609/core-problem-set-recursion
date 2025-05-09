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
def digit_match(num1, num2):
    if num1 == 0 and num2 == 0:
        return 1

    def inner(n1, n2):
        if n1 == 0 or n2 == 0:
            return 0
        match = 1 if n1 % 10 == n2 % 10 else 0
        return match + inner(n1 // 10, n2 // 10)

    return inner(num1, num2)

