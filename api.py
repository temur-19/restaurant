from fastapi import APIRouter, Depends ,HTTPException
from database import Base, engine,get_db
from sqlalchemy.orm import Session, Mapped
from sqlalchemy import select
from schemas import OrderCreate, OrderItemBase, OrderOut ,OutOrderItem ,CreateOrderItem,OutCategory,CreateCategore, OutMenuItems , CreateMenuItems, UpdateOrderItem
from models import Category, MenuItem, Order, OrderItem
from typing import List

api_router = APIRouter(prefix='/api/orders')

@api_router.post('/category', response_model=OutCategory)
def create_category(category_in:CreateCategore, db:Session = Depends(get_db)):
    category = Category(**category_in.model_dump())
    db.add(category)
    db.commit()
    db.refresh(category)
    return category



@api_router.get('/category', response_model=List[OutCategory])
def get_category(db:Session = Depends(get_db)):
    stmt  = select(Category)
    category = db.scalars(stmt).all()
    return category


@api_router.post('/menuitems', response_model = OutMenuItems)
def create_menuitems(menuitem_in:CreateMenuItems, db:Session = Depends(get_db)):    
    menuitem  = MenuItem(**menuitem_in.model_dump())
    db.add(menuitem)
    db.commit()
    db.refresh(menuitem)
    return menuitem



@api_router.get('/menuitems', response_model=List[OutMenuItems])
def get_menuItems(db:Session = Depends(get_db)):
    stmt  = select(MenuItem)
    menuitem = db.scalars(stmt).all()
    return menuitem


@api_router.post('/order', response_model=OrderOut)
def create_order(order_in:OrderCreate, db:Session = Depends(get_db)):
    order = Order(**order_in.model_dump())
    db.add(order)
    db.commit()
    db.refresh(order)
    return order



@api_router.get('/order', response_model=List[OrderOut])
def get_order(db:Session = Depends(get_db)):
    stmt  = select(Order)
    order = db.scalars(stmt).all()
    return order


@api_router.post('/orderitem', response_model=OutOrderItem)
def create_orderItem(orderItem_in: CreateOrderItem, db:Session = Depends(get_db)):
    menu_item = db.query(MenuItem).filter(MenuItem.id == orderItem_in.menu_item).first()
    if not menu_item:
            raise HTTPException(status_code=404, detail="Menu item topilmadi")
    total1 = menu_item.price * orderItem_in.quantity

    orderItem = OrderItem(
            menu_item=orderItem_in.menu_item,
            quantity=orderItem_in.quantity,
            order_id=orderItem_in.order_id,
            total=total1
        )
    db.add(orderItem)
    db.commit()
    db.refresh(orderItem)
    return orderItem


@api_router.put('/orderitem{orderitem_id}', response_model=OutOrderItem)
def update_orderitem(orderitem_in:UpdateOrderItem, orderitem_id, db:Session = Depends(get_db)):
    stmt = select(OrderItem).where(OrderItem.id == orderitem_id)
    orderitem:OrderItem = db.scalar(stmt)
    if not orderitem:
        raise HTTPException(status_code=404, detail=f'{orderitem_id} id li order item mavjud emas')
    
    orderitem.menu_item = orderitem_in.menu_item
    orderitem.quantity = orderitem_in.quantity

    db.add(orderitem)
    db.commit()
    db.refresh(orderitem)
    return orderitem

@api_router.delete('/orderitem{orderitem_id}')
def delete_orderitem(orderitem_id, db:Session = Depends(get_db)):
    stmt = select(OrderItem).where(OrderItem.id == orderitem_id)
    orderitem = db.scalar(stmt)
    if not orderitem:
        raise HTTPException (status_code=404, detail=f'{orderitem_id} id li orderitem yoq')
    
    db.delete(orderitem)
    db.commit()
    return {'status':"Muvaffaqiyati o'chirildi"}


@api_router.get('/orderitem', response_model=List[OutOrderItem])
def get_orderItem(db:Session = Depends(get_db)):
    stmt  = select(OrderItem)
    orderItem = db.scalars(stmt).all()
    return orderItem




