"""
直接导入quantaxis 太麻烦了，直接写数据库
"""
import pymongo

__default_db_uri__ = 'mongodb://localhost:27017'


def mongo_client(uri=__default_db_uri__):
    client = pymongo.MongoClient(uri)
    return client
