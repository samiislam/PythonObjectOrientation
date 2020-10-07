"""
Object-Oriented Python code for a rebuy shop
"""
from object_oriented_computer_shop import ComputerShop, ItemNotFound
from computer import Computer
from typing import Optional


class RebuyShop(ComputerShop):

    def print_item(self, item_id: int) -> None:
        if item_id in self.inventory:
            print(f'Rebuy Shop: {self.inventory[item_id]}')
        else:
            print(f'Item not found in the Rebuy Shop')

    def refurbish(self, item_id: int, new_os : Optional[str] = None) -> None:
        if item_id in self.inventory:
            self.__refurbish(item_id)

            if new_os is not None:
                self.__set_new_os(item_id, new_os)
        else:
            raise ItemNotFound

    # pseudo-private method
    def __refurbish(self, item_id: int) -> None:
        computer : Computer = self.inventory[item_id]
        
        if computer.year_made < 2000:
            computer.set_price(0)
        elif computer.year_made < 2010:
            computer.set_price(250)
            #computer._Computer__price = 8
        elif computer.year_made < 2018:
            computer.set_price(650)
        else:
            computer.set_price(1000)

    # pseudo-private method
    def __set_new_os(self, item_id: int, new_os: str) -> None:
        computer : Computer = self.inventory[item_id]
        computer.set_os(new_os)
