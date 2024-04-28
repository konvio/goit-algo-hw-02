from collections import deque


def is_palindrome(input):
    my_deque = deque()
    for char in input:
        if char.isalnum():
            my_deque.append(char.lower())

    while len(my_deque) > 1:
        if my_deque.popleft() != my_deque.pop():
            return False

    return True

# Test cases
print(is_palindrome("A man, a plan, a canal: Panama"))  # Should return True
print(is_palindrome("race car"))  # Should return True
print(is_palindrome("not a palindrome"))  # Should return False