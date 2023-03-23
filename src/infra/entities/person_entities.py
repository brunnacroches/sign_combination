from sqlalchemy import Column, String, Integer
from src.infra.configs.base import Base

class Person(Base):
    __tablename__ = 'person'
    
    id_user = Column(Integer, primary_key=True, autoincrement=True)
    name_user = Column(String(50), nullable=False)
    zodiac_sign = Column(String(100), nullable=False)
    
    def to_dict(self):
        return {
            "id_user": self.id_user,
            "name_user": self.name_user,
            "zodiac_sign": self.zodiac_sign
        }
