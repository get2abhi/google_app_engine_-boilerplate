# google_app_engine_-boilerplate
boilerplate code for google app engine project in python which includes many useful libraries 


# Keyczar

How to use keyczar for encryption and decryption

## Create keys first


```
mkdir -p /tmp/kz 
keyczart create --location=/tmp/kz --purpose=crypt 
keyczart addkey --location=/tmp/kz --status=primary 
```


Python code to encrypt and decrypt


```
from keyczar import keyczar

s = 'secret string'
location = '/tmp/kz'
crypter = keyczar.Crypter.Read(location)
s_encrypted = crypter.Encrypt(s)
s_decrypted = crypter.Decrypt(s_encrypted)
print s
print s_encrypted
print s_decrypted
```
