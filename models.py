from sqlalchemy import String, Integer, ForeignKey, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List
from database import Base


class Categories(Base):
    __tablename__ = 'category'
    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    name:Mapped[str] = mapped_column(String(length=100), nullable=False)
    menuitem:Mapped['MenuItems'] = relationship(back_populates='category', cascade='all, delete-orphan')


class MenuItems(Base):
    __tablename__ = 'menuitem'
    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    name:Mapped[str] = mapped_column(String(length=100), nullable=False)
    price = mapped_column(Numeric(precision=10,scale=2))
    category_id:Mapped[int]  = mapped_column(ForeignKey('category.id'))
    description:Mapped[str] = mapped_column(String(length=200))
    category:Mapped['Categories'] = relationship(back_populates='menuitem')
    orderitem:Mapped['OrderItems'] = relationship(back_populates='menuitem')


class Orders(Base):
    __tablename__ = 'order'
    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    address:Mapped[str] = mapped_column(String(length=400), nullable=False)
    total = mapped_column(Numeric(precision=10,scale=2))
    phone_number:Mapped[str] = mapped_column(String(length='20'),nullable=False)
    orderitem = relationship('OrderItems', back_populates='order')
    



class OrderItems(Base):
    __tablename__ = 'orderitem'
    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    menu_item:Mapped[int] = mapped_column(ForeignKey('menuitem.id'))
    quantity:Mapped[int] = mapped_column(Integer, default=0)
    total = mapped_column(Numeric(precision=10, scale=2))
    order_id = mapped_column(ForeignKey('order.id'), unique=True)
    order = relationship("Orders", back_populates="orderitem")    
    menuitem:Mapped[List['MenuItems']] = relationship(back_populates='orderitem')


