def is_palindrome(string):
    string = string.lower()  # convert the string to lowercase
    left = 0  # initialize the left index
    right = len(string) - 1  # initialize the right index

    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1

    return True
