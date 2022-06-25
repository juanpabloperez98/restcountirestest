import hashlib


def encrypt(countrie):
    str_encoded = countrie.encode()
    hash_object = hashlib.sha1(str_encoded)
    pbHash = hash_object.hexdigest()
    return pbHash