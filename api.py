from fastapi import APIRouter, Depends
from database import Base, engine,get_db
from sqlalchemy.orm import Session
from sqlalchemy import select
from schemas import OrderCreate, OrderItemBase, OrderOut ,OutOrderItem ,CreateOrderItem,OutCategory,CreateCategore, OutMenuItems , CreateMenuItems
from models import Categories, MenuItems
from typing import List

Base.metadata.create_all(bind = engine)

api_router = APIRouter(prefix='/api/orders')

@api_router.post('/orders', response_model=OutCategory)
def create_category(category_in:CreateCategore, db:Session = Depends(get_db)):
    category = Categories(**category_in.model_dump())
    db.add(category)
    db.commit()
    db.refresh(category)
    return category

# @api_router.get('/menuitems', response_model=List[OutMenuItems])
# def out_menuitems(db:Session = Depends(get_db)):
#     stmt= select(Categories)
#     menuitems = db.scalars(stmt).all()
#     return menuitems

@api_router.post('/menuitems', response_model = OutMenuItems)
def create_menuitems(menuitem_in:CreateMenuItems, db:Session = Depends(get_db)):
    menuitem  = MenuItems(**menuitem_in.model_dump())
    db.add(menuitem)
    db.commit()
    db.refresh(menuitem)
    return menuitem


