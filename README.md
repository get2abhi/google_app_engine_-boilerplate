# google_app_engine_boilerplate
boilerplate code for google app engine project in python which includes many useful libraries 

# Libraries

## Keyczar

How to use keyczar for encryption and decryption

### Create keys first


```
mkdir -p ./tmp/kz 
python keyczart.py create --location=./tmp/kz --purpose=crypt --name=DUMMY
python keyczart.py addkey --location=./tmp/kz --status=primary 
```


Python code to encrypt and decrypt


```
from keyczar import keyczar

s = 'secret string'
location = './tmp/kz'
crypter = keyczar.Crypter.Read(location)
s_encrypted = crypter.Encrypt(s)
s_decrypted = crypter.Decrypt(s_encrypted)
print s
print s_encrypted
print s_decrypted
```

Android code to encrypt

https://github.com/get2abhi/Keyczar_Android_Demo
