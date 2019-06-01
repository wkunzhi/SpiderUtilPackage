# -*- coding: utf-8 -*-
# __author__ = "zok"  362416272@qq.com
# Date: 2019-04-28  Python: 3.7

import base64
import zlib
import json
from datetime import datetime


class Translation(object):

    @staticmethod
    def load_base64(_key):
        """解base64"""
        return base64.b64decode(_key)

    @staticmethod
    def load_zlib(_key):
        """解压流"""
        return zlib.decompress(_key)

    @staticmethod
    def load_str(_key):
        return str(_key, encoding="utf-8")

    @staticmethod
    def load_hex(_key):
        """转到16进制"""
        return _key.hex()

    @staticmethod
    def go_16_10(_key):

        return _key.hex(10)

    @staticmethod
    def hex_to_str(_key):
        return ''.join([chr(i) for i in [int(b, 16) for b in _key.split(' ')]])

    @staticmethod
    def bin_to_str(_key):
        return ''.join([chr(i) for i in [int(b, 2) for b in _key.split(' ')]])


if __name__ == '__main__':

    key = 'YyJr8BeAz5P07Lf/Dp2us2CYTYYLk4VmKCOrFfeAgB8u4wA/y9F+lT19vsPeFxnCBzH/myCrIeeJ52nzShYKmulf1+Fl6H6R2pg4NbBnIKMo9L1xcFcmF2e9vCPaJ8X70r2CtKXny8lP9KBVDkSz9w=='

    ts = Translation()
    a1 = ts.load_base64(key)
    print(a1)
    a2 = ts.load_hex(a1)
    print(a2)


    print(int('f7', 16))


