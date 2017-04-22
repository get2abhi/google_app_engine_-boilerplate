import keyczar

s = 'secret string'
location = './tmp/kz'
crypter = keyczar.Crypter.Read(location)
s_encrypted = crypter.Encrypt(s)
s_decrypted = crypter.Decrypt(s_encrypted)
print s
print s_encrypted
print s_decrypted
