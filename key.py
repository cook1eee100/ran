from Cryptodome.PublicKey import RSA
import os

if not os.path.isdir('c:/key'):
    os.mkdir('C:/key')

key = RSA.generate(2048)

# private key 생성
private_key = key.export_key()
with open('C:/key/private.pem', 'wb') as f:
    f.write(private_key)

# public key 생성
public_key = key.publickey().export_key()
with open('C:/key/public.pem', 'wb') as f:
    f.write(public_key)


