""" ORM  O 用于生成数据库中的表"""
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
engine = create_engine("mysql+mysqlconnector://root:123456@localhost/userdb",
                                    encoding='utf8', echo=True)
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base(bind=engine)

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    username = Column(String(20), nullable=False)
    password = Column(String(20),nullable=False)

class List1(Base):
    __tablename__ = "list"
    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    name = Column(String(20), nullable=False)
    detail = Column(String(1000), nullable=False)
    uid = Column(Integer, ForeignKey("user.id"), nullable=False)


# 创建所有的东西
if __name__ == "__main__":
    Base.metadata.create_all()
