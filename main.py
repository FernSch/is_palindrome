def is_palindrome(str):
    #idk wtf ::-1 is but is reverses lists so 👍👍
    try:
        return True if list(str) == (list(str))[::-1] else False
    except TypeError:
        raise Exception("must be of type STRING")


