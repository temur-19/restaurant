from sqlalchemy import String, Integer, ForeignKey, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List
from database import Base


class Category(Base):
    __tablename__ = 'categorys'
    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    name:Mapped[str] = mapped_column(String(length=100), nullable=False)
    menuitem:Mapped[List['MenuItem']] = relationship(back_populates='category', cascade='all, delete-orphan')


class MenuItem(Base):
    __tablename__ = 'menuitems'
    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    name:Mapped[str] = mapped_column(String(length=100), nullable=False)
    price = mapped_column(Numeric(precision=10,scale=2))
    category_id:Mapped[int]  = mapped_column(ForeignKey('categorys.id'))
    description:Mapped[str] = mapped_column(String(length=200))
    category:Mapped['Category'] = relationship(back_populates='menuitem')
    orderitem:Mapped['OrderItem'] = relationship(back_populates='menuitem')


class Order(Base):
    __tablename__ = 'orders'
    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    address:Mapped[str] = mapped_column(String(length=400), nullable=False)
    total = mapped_column(Numeric(precision=10,scale=2))
    phone_number:Mapped[str] = mapped_column(String(length=20),nullable=False)
    status:Mapped[str] = mapped_column(String(length=20))
    orderitem:Mapped[List['OrderItem']] = relationship('OrderItem', back_populates='orders')
    



class OrderItem(Base):
    __tablename__ = 'orderitems'
    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    menu_item:Mapped[int] = mapped_column(ForeignKey('menuitems.id'))
    quantity:Mapped[int] = mapped_column(Integer, default=0)
    total = mapped_column(Numeric(precision=10, scale=2))
    order_id: Mapped[int] = mapped_column(ForeignKey('orders.id'))
    orders: Mapped['Order'] = relationship("Order", back_populates="orderitem") 
    menuitem:Mapped['MenuItem'] = relationship(back_populates='orderitem')


