def is_palindrome(str):
    try:
        return True if list(str) == (list(str))[::-1] else False
    except TypeError:
        raise Exception("must be of type STRING")


