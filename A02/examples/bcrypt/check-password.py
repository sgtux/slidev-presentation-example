import bcrypt

password = '123qwe'

hashed = '$2b$12$WpQd/eHpjbvnOGoZzCrHVeMBRwDLuQTe686hHXWWAouDda3DDNT6a'

if bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8')):
    print('Sucesso!')
else:
    print('Senha inválida!')