import json
from decimal import Decimal

from sqlalchemy.orm import DeclarativeMeta


class Serializable_Conversion(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}
            # 过滤无效字段
            for field in [x for x in dir(obj) if
                          not x.startswith('_') and x != 'metadata' and x != 'query' and x != 'query_class']:
                data = obj.__getattribute__(field)
                try:
                    # 判断类型 因为该类型无法序列化  所以强转为字符串 其他类型也是真么写 添加一下就可以
                    if isinstance(data, Decimal):
                        fields[field] = str(data)
                    elif data == None:
                        fields[field] = ''
                    else:
                        json.dumps(data)
                        fields[field] = data
                except TypeError:

                    fields[field] = str(data)
            # a json-encodable dict
            return fields

        return json.JSONEncoder.default(self, obj)
