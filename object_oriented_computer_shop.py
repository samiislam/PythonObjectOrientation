"""
Object-Oriented Python code for a computer shop
"""
from typing import Dict
from computer import Computer

class ItemNotFound(Exception):
    ...

class ComputerShop():

    def __init__(self) -> None:
        self.inventory: Dict[int, Computer] = {}
        self.item_id: int = 0

    def buy(self, computer :  Computer) -> int:
        self.item_id =+ 1
        self.inventory[self.item_id] = computer
        return self.item_id

    def update_price(self, item_id: int, new_price: int) -> None:
        if item_id in self.inventory:
            self.inventory[item_id].set_price(new_price)
        else:
            raise ItemNotFound

    def sell(self, item_id: int) -> None:
        if item_id in self.inventory:
            del self.inventory[item_id]
        else:
            raise ItemNotFound

    def print_item(self, item_id: int) -> None:
        if item_id in self.inventory:
            print(f'Computer Shop: {self.inventory[item_id]}')
        else:
            print(f'Item not found in the Computer Shop')

    @classmethod
    def get_header(cls) -> str:
        return cls.__name__