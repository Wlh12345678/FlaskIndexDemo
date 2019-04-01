# 操作orm model  写在main里面，代码太多
from FlaskIndexDemo.orm import model
from sqlalchemy import create_engine
engine = create_engine("mysql+mysqlconnector://root:123456@localhost/userdb",
                                    encoding='utf8', echo=True)

from sqlalchemy.orm import  sessionmaker
session = sessionmaker()()

def insterUser(username,password):
    session.add(model.User(username=username,password=password))
    session.commit()
    session.close()
def checkUser(username,password):
    # result代表用户的 username ，查询 username 是否存在
    result = session.query(model.User).filter(model.User.username == username).filter(model.User.password == password).first().username
    print(result, '查询用户id，判断登录')
    if result:
        return result
    else:
        return -1

def checkList():
    result = session.query(model.List1).all()
    return result

def insterList(name,detail):
    session.add(model.List1(name=name, detail=detail,uid=session.query(model.User).filter(model.User.username).first().id))
    session.commit()
    session.close()

def checkDetail(id):
    res = session.query(model.List1).filter(model.List1.id==id).first()
    return res

if __name__ == "__main__":
    insterUser("1","1")
    insterList("1","1")
