from database import Base
from sqlalchemy import Column,String,Integer,Boolean,Text,ForeignKey
from sqlalchemy_utils.types import ChoiceType
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__="user"
    id = Column(Integer,primary_key=True)
    username = Column(String(30),unique=True)
    email = Column(String(70),unique=True)
    password = Column(Text,nullable=True)
    is_staff = Column(Boolean,default=False)
    is_active = Column(Boolean,default=False)
    order = relationship("Order",back_populates="user")

    def  __repr__(self):
        return f"<User{self.username}"


class Order(Base):
    ORDER_STATUSES=(
        ('PENDING','pending'),
        ('IN-TRANSIT','in-transit'),
        ('DELIVERED','delivered'),
    )
    __tablename__="orders"
    id = Column(Integer,primary_key=True)
    quantity = Column(Integer,nullable=False)
    order_status = Column(ChoiceType(choices=ORDER_STATUSES),default="PENDING")
    user_id = Column(Integer,ForeignKey('user.id'))
    user = relationship("User",back_populates='order')

    def __repr__(self):
        return f"<Order {self.id}"