from pydantic import BaseModel, Field


class CategoryBase(BaseModel):
    name:str = Field(max_length=100)

class CreateCategore(CategoryBase):
    pass 

class OutCategory(CategoryBase):
    pass

class MenuItemBase(BaseModel):
    name:str = Field(max_length=100)
    price:float  = Field()
    category_id:int = Field()
    description:str = Field(max_length=200)

class CreateMenuItems(MenuItemBase):
    pass 

class  OutMenuItems(MenuItemBase):
    pass

class OrderItemBase(BaseModel):
    menu_item:int = Field()
    quantity:int = Field()
    total:float  = Field()

class CreateOrderItem(OrderItemBase):
    pass 

class OutOrderItem(OrderItemBase):
    pass


class OrderBase(BaseModel):
    address:str = Field()
    total:float = Field()
    status: str = Field()

class OrderCreate(OrderBase):
    pass 

class OrderOut(OrderBase):
    pass

