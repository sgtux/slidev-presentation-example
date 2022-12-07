- Algoritmo de criptografia quebrado ou arriscado
- Uso de senha armazenadas em código
- Entripia insuficiente

Como provinir ?

- Classificar dados processados, armazenados e transmitidos pela aplicação. Identificar quais dados são sensíveis de acordo com as leis de privacidade, requisitos regulamentares ou necessidades de negócio.
...

openssl req -x509 -nodes -days 365 -sha256 -newkey rsa:2048 -keyout mykey.pem -out mycert.pem

openssl s_server -cert mycert.pem -www

openssl enc -base64 -in arq1.txt -out arq1.txt.enc

openssl enc -aes-256-cbc -a -salt -in arq1.txt -out arq1.txt.enc
openssl enc -d -aes-256-cbc -a -salt -in arq1.txt.enc -out arq2.txt

openssl genrsa -aes128 -out alice-private.pem 1024
openssl rsa -in alice-private.pem -pubout > alice-public.pem


openssl genrsa -aes128 -out bob-private.pem 1024
openssl rsa -in bob-private.pem -pubout > bob-public.pem


openssl pkeyutl -encrypt -inkey bob-public.pem -pubin -in alice-to-bob.txt -out alice-to-bob.txt.enc

openssl pkeyutl -decrypt -inkey bob_private.pem -in top_secret.enc > top_secret.txt