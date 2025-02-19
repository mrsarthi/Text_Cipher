import random
import string

chars = " " + string.ascii_letters + string.punctuation + string.digits
chars = list(chars)
key = chars.copy()
random.shuffle(key)


def encrypt(text):
    cipher = ""
    for i in text:
        ind = chars.index(i)
        cipher += key[ind]
    return cipher


def decrypt(text):
    original = ""
    for i in text:
        ind = key.index(i)
        original += chars[ind]
    return original
