from pydantic import BaseModel, Field


class CategoryBase(BaseModel):
    name:str = Field(max_length=100)

class CreateCategore(CategoryBase):
    pass 

class OutCategory(CategoryBase):
    id: int = Field(ge=1)
    pass

class MenuItemBase(BaseModel):
    name:str = Field(max_length=100)
    price:float  = Field()
    category_id:int = Field()
    description:str = Field(max_length=200) 

class CreateMenuItems(MenuItemBase):
    pass 

class  OutMenuItems(MenuItemBase):
    id:int = Field(ge = 1)
    pass

class OrderItemBase(BaseModel):
    menu_item:int = Field()
    quantity:int = Field()
    total:float  = Field()
    order_id:int = Field()

class CreateOrderItem(OrderItemBase):
    pass

class OutOrderItem(OrderItemBase):
    id:int = Field(ge = 1)
    pass

class UpdateOrderItem(OrderItemBase):
    pass


class OrderBase(BaseModel):
    address:str = Field()
    total:float = Field()
    phone_number:str = Field()
    status: str = Field()

class OrderCreate(OrderBase):
    pass 

class OrderOut(OrderBase):
    id:int = Field(ge = 1 )
    pass

