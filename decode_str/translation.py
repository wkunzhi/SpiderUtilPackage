# -*- coding: utf-8 -*-
# __author__ = "zok"  362416272@qq.com
# Date: 2019-04-28  Python: 3.7

import base64
import zlib


class TranslationMetaClass(type):
    """Meta 类"""
    def __new__(mcs, name, bases, attrs):
        count = 0
        attrs['__decode__'] = []
        for k, v in attrs.items():
            if 'decode_' in k:
                attrs['__decode__'].append(k)
                count += 1
        attrs['__TranslationFuncCount__'] = count
        return type.__new__(mcs, name, bases, attrs)


class Decode(object):

    def decode_base64(self):
        """解base64"""
        self._key = base64.b64decode(self._key)

    def decode_zlib(self):
        """解压串"""
        self._key = zlib.decompress(self._key)

    def decode_str(self):
        """转字符串"""
        return str(self._key, encoding="utf-8")

    def decode_hex(self):
        """转到16进制"""
        self._key = self._key.hex()


class Translation(Decode, metaclass=TranslationMetaClass, ):

    def __init__(self, _key):
        self._key = _key

    def main(self):
        choice = self.msg()
        while choice != 'e':
            if choice == '1':
                self.decode_base64()
            elif choice == '2':
                self.decode_zlib()
            elif choice == '3':
                self.decode_hex()
            self._print('blue', self._key)
            choice = self.msg()

        self._print('red', '调试结束')

    def msg(self):
        msg = """
        1. base64 解码
        2. 解压字符串
        3. 转 16 进制
        
        b: 【返回上个选择】  e: 【退出】
        """
        self._print('yellow', msg)
        return input('请选择').lower()

    @staticmethod
    def _print(color, msg):
        """打印颜色控制
        """
        node = '\033[1;3{id}m{msg}\033[0m'
        if color == 'yellow':
            print(node.format(id=3, msg=msg))
        elif color == 'red':
            print(node.format(id=1, msg=msg))
        elif color == 'green':
            print(node.format(id=2, msg=msg))
        elif color == 'blue':
            print(node.format(id=4, msg=msg))
        else:
            print(node.format(id=7, msg=msg))


if __name__ == '__main__':
    key = 'YyJr8BeAz5P07Lf/Dp2us2CYTYYLk4VmKCOrFfeAgB8u4wA/y9F+lT19vsPeFxnCBzH/myCrIeeJ52nzShYKmulf1+Fl6H6R2pg4NbBnIKMo9L1xcFcmF2e9vCPaJ8X70r2CtKXny8lP9KBVDkSz9w=='
    _key = input('\033[1;31m输入解码内容>>> \033[0m')
    ts = Translation(key)
    ts.main()
