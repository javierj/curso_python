__author__ = 'Javier'


import re

def verify(password):
    if len(password) < 6:
        return False
    if '_' not in password:
        return False
    if _notContainsNumber(password):
        return False
    if _notContainsLetters(password):
        return False

    return True


def _notContainsNumber(password):
    result = re.search("[0-9]", password)
    if result is None:
        return True

def _notContainsLetters(password):
    result = re.search("[a-zA-Z]", password)
    if result is None:
        return True
