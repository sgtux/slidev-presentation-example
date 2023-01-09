import bcrypt

password = '123qwe'

# hashed = '$2b$12$0Vdyndtpn3vlLKCFB1pvT.O.qrykX6dyaVhZwwrybGBpVrH22b8UG'
hashed = '$2b$12$WOaUQnZOeAiFFOIGDAod1.Sql/jGTg6JClfXE0LydGoLIMejkQSvE'

if bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8')):
    print('Sucesso!')
else:
    print('Senha inválida!')