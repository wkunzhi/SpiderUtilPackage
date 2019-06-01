# -*- coding: utf-8 -*-
# __author__ = "zok"  362416272@qq.com
# Date: 2019-04-28  Python: 3.7

import base64
import zlib

COLOR = {'red': 1, 'green': 2, 'yellow': 3, 'blue': 4}


class TranslationMetaClass(type):
    """Meta 类"""
    def __new__(mcs, name, bases, attrs):
        count = 0
        attrs['__Decode__'] = {}
        for k, v in attrs.items():
            if 'decode_' in k:
                count += 1
                attrs['__Decode__'][str(count)] = k
        attrs['__TranslationFuncCount__'] = count
        return type.__new__(mcs, name, bases, attrs)


class Util(object):
    """辅助类"""

    @staticmethod
    def _print(color, msg):
        """print color control
        """
        node = '\033[1;3{id}m{msg}\033[0m'
        if COLOR.get(color):
            print(node.format(id=COLOR.get(color), msg=msg))
        else:
            print(msg)

    def msg(self):
        """print decode func
        """
        for k in self.__Decode__:
            self._print('yellow', str(k) + ': ' + self.__Decode__[k][7:])
        print('b: 【返回】  e: 【退出】')
        return input('请选择>>>').lower()


class Decode(Util, metaclass=TranslationMetaClass):
    """
    将需要添加的转码类型按下列类似格式添加即可
    def decode_自定义名(self):
        self._key = 解密过程
    """
    def __init__(self, _key):
        self._key = _key

    def main(self):
        choice = self.msg()
        while choice != 'e':
            if choice in self.__Decode__:  # 选择是否在现有函数选项中
                # 字符串转函数运行
                try:
                    eval("self.{}()".format(self.__Decode__[choice]))
                except Exception as e:
                    self._print('red', '该方法解码失败，请换一种')
            self._print('blue', self._key)
            choice = self.msg()
        self._print('red', '调试结束')

    def decode_base64(self):
        """解base64"""
        self._key = base64.b64decode(self._key)

    def decode_zlib(self):
        """解压串"""
        self._key = zlib.decompress(self._key)

    def decode_str(self):
        """转字符串"""
        self._key = str(self._key, encoding="utf-8")

    def decode_hex(self):
        """转到16进制"""
        self._key = self._key.hex()


if __name__ == '__main__':
    _key = 'YyJr8BeAz5P07Lf/Dp2us2CYTYYLk4VmKCOrFfeAgB8u4wA/y9F+lT19vsPeFxnCBzH/myCrIeeJ52nzShYKmulf1+Fl6H6R2pg4NbBnIKMo9L1xcFcmF2e9vCPaJ8X70r2CtKXny8lP9KBVDkSz9w=='
    # _key = input('\033[1;31m输入解码内容>>> \033[0m')
    ts = Decode(_key)
    ts.main()
