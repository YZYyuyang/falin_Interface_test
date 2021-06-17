
import hashlib
from Crypto.Cipher import AES
from base64 import b64decode, b64encode
import base64

class Encryption3():

    def __init__(self):
        self.aes_key = 'imlaw1dmgbsj2cm9'
        self.mode = AES.MODE_CBC
        self.iv = b'cdkjytgsrj754921'
        self.unpad = lambda s: s[:-ord(s[len(s) - 1:])]
        self.key = 'bc37cc63-9d14-4013-8255-9168f24ceacd'

    # MD5加密方法
    def md5_encrypt(self, data):
        md5 = hashlib.md5()  # 创建对象
        sign_bytes_utf8 = data.encode(encoding="utf-8")
        md5.update(sign_bytes_utf8)
        sign_md5 = md5.hexdigest()
        return sign_md5

    # 管理端data
    def base_64_lock(self,data):
        base_data = base64.b64encode(data.encode('utf-8')).decode('utf-8')
        return base_data

    # 管理端sign
    def cms_sign(self,data):
        sign = self.base_64_lock(data)+self.key
        return self.md5_encrypt(sign)

    # 客户端sign
    def app_aes_sign(self,dic):
        BLOCK_SIZE = AES.block_size
        pad = lambda s: s + (BLOCK_SIZE - len(s.encode()) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s.encode()) % BLOCK_SIZE)
        text = pad(str(dic)).encode()  # 包pycryptodome 的加密函数不接受str
        cipher = AES.new(key=self.aes_key.encode('utf-8'), mode=AES.MODE_CBC, IV=self.iv)
        encrypted_text = cipher.encrypt(text)
        # 进行64位的编码,返回得到加密后的bytes，decode成字符串
        sign = b64encode(encrypted_text).decode('utf-8')+self.key
        return self.md5_encrypt(sign)

    # 客户端data
    def app_aes_data(self,dic):
        BLOCK_SIZE = AES.block_size
        pad = lambda s: s + (BLOCK_SIZE - len(s.encode()) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s.encode()) % BLOCK_SIZE)
        text = pad(str(dic)).encode()  # 包pycryptodome 的加密函数不接受str
        cipher = AES.new(key=self.aes_key.encode('utf-8'), mode=AES.MODE_CBC, IV=self.iv)
        encrypted_text = cipher.encrypt(text)
        return b64encode(encrypted_text).decode('utf-8')

    # 客户端data解密
    def app_aes_decrypt(self,str):
        try:
            if str == '':
                print('')
            else:
                encrypted_text = b64decode(str)
                cipher = AES.new(key=self.aes_key.encode(), mode=AES.MODE_CBC, IV=self.iv)
                decrypted_text = cipher.decrypt(encrypted_text)
                print('客户端参数data解密结果：', self.unpad(decrypted_text).decode('utf-8'))
        except:
            print('客户端参数data无法解密：')

    # 管理端data解密
    def cms_debase64(self,data=''):

        try:
            if data == '':
                print('')
            else:
                result = base64.b64decode(data).decode('utf-8')
                print('管理端参数data解密结果：',result)
        except:
            print('管理端参数data无法解密：')

if __name__ == '__main__':
    e = Encryption3()


    # 加密参数
    data = "{'phone':'13281803775'}"
    # 解密参数
    decode = 'eydwaG9uZSc6JzEzMjgxODAzNzc1J30='


    # 管理端sign/data
    data_1 = e.base_64_lock(data)
    print('\n管理端data：',data_1)
    sign = e.cms_sign(data)
    print('管理端sign：',sign)
    # 客户端data/sign
    data_3 = e.app_aes_data(data)
    print('客户端data：', data_3)
    data_2 = e.app_aes_sign(data)
    print('客户端sign：',data_2)
    e.cms_debase64(decode)
    e.app_aes_decrypt(decode)


