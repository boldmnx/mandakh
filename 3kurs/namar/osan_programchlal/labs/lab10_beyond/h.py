import hashlib

hash256 = hashlib.sha256()
hash256.update('some'.encode('utf-8'))
hashPass = hash256.hexdigest()
print( hashPass)
