# -*- coding: utf-8 -*-
# __author__ = "zok"  362416272@qq.com
# Date: 2019-05-15  Python: 3.7

from DataMigration.db.MongoDB import Mongo
from DataMigration.db.Mysql import Mysql


class Migrate(object):
    def __init__(self, mongodb_name,collection):
        self.mongo = Mongo(mongodb_name, collection)
        self.mysql = Mysql()

