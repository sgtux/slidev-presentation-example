import hashlib

password = '123qwe'
salt = 'owasp'

hashed = hashlib.sha1(password.encode('utf-8')).hexdigest()
hashed_salted = hashlib.sha1(f'{password}{salt}'.encode('utf-8')).hexdigest()

print(f'         Hash SHA1: {hashed}')
print(f'Hash SHA1 com salt: {hashed_salted}')
