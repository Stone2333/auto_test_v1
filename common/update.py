from common import DB
from config import setting


def db():
    """
    数据库对象

    :return:数据库对象
    """
    d = DB.OracleDB(
        username=setting.DevConfig.username,
        password=setting.DevConfig.password,
        host=setting.DevConfig.dbhost)
    return d

