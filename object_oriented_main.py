"""
Program for object-oriented code
"""
from computer import Computer
from object_oriented_computer_shop import ComputerShop
from object_oriented_rebuy_shop import RebuyShop

def use_object_oriented() -> None:

    print('CREATE COMPUTER')
    computer: Computer = Computer('Zeta 2000RC', 
                            "2.4 GHz Quad‑Core Intel Core i7",
                            128, 16, 
                            "OpenBSD", 2004, 1067)

    print(computer)

    print(f'\n{ComputerShop.get_header()}')
    print('#' * 20)
    shop : ComputerShop = ComputerShop()
    
    print('BUY')
    item1 : int = shop.buy(computer)
    shop.print_item(item1)
    
    print('UPDATE PRICE')
    shop.update_price(item1, 1050)
    shop.print_item(item1)
    
    print('SELL')
    shop.sell(item1)
    
    print('PRINT AFTER SELLING')
    shop.print_item(item1)
    #print('UPDATE PRICE AFTER SELLING')
    #shop.update_price(item1, 2000) # This is not possible!!

    rshop : RebuyShop = RebuyShop()
    print(f'\n{RebuyShop.get_header()}')
    print('#' * 20)

    print('R BUY')
    item2: int = rshop.buy(computer)
    rshop.print_item(item2)
    
    print('REFURBISH')
    rshop.refurbish(item2, 'Linux Mint')
    rshop.print_item(item2)
    
    print('R SELL')
    rshop.sell(item2)
    
    print('PRINT AFTER R SELLING')
    rshop.print_item(item2)
    
    print('UPDATE PRICE AFTER R SELLING')
    rshop.update_price(item2, 2000) # This is not possible!!
