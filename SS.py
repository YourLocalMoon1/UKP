from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
class Encryption:
    def __init__(self, genKey = True):
        if genKey:
            self.SetupKey()
        else:
            pass
    def SetupKey(self):
        key = RSA.generate(2048)
        private_key = key.exportKey("PEM")
        public_key = key.publickey().exportKey("PEM")
        fd = open("private_key.pem", "wb")
        fd.write(private_key)
        fd.close()
        fd = open("public_key.pem", "wb")
        fd.write(public_key)
        fd.close()
    def getPublicCipher(self) -> PKCS1_OAEP.PKCS1OAEP_Cipher:
        try:
            key = RSA.import_key(open('public_key.pem').read())
            return PKCS1_OAEP.new(key)
        except FileNotFoundError:
            self.SetupKey()
            raise RuntimeWarning("No public key found, feel free to ignore this warning if it's a server, or your first time!")
    def getPrivateCipher(self) -> PKCS1_OAEP.PKCS1OAEP_Cipher:
        try:
            key = RSA.import_key(open('private_key.pem').read())
            return PKCS1_OAEP.new(key)
        except FileNotFoundError:
            self.SetupKey()
            raise RuntimeError("No private key found, a private key is necessary!")
    def Encrypt(self, text: str):
        return self.getPublicCipher().encrypt(text.encode())
    def Decrypt(self, text):
        return self.getPrivateCipher().decrypt(text)

if __name__ == "__main__":
    Enc = Encryption(genKey=False)
    a = Enc.Encrypt("Hello")
    print(f"Encrypted: {a}")
    a = Enc.Decrypt(a)
    print(f"Decrypted: {a}")


### Key generating server ###
### Used for encryption! ###