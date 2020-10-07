"""
Object-Oriented code to represent a computer
"""

class Computer:

    # dunder method - ctor
    def __init__(self, description: str, 
                processor_type: str, hard_drive_capacity: int, 
                memory: int, os: str,
                made_in_year: int, price: int) -> None:

        # pseudo-private attributes
        self.__description = description
        self.__processor_type = processor_type
        self.__hard_drive_capacity = hard_drive_capacity
        self.__memory = memory
        self.__os = os
        self.__made_in_year = made_in_year
        self.__price = price

    # dunder method
    def __str__(self) -> str:
        return f'<Computer: {self.__description}, Price: {self.__price}, OS: {self.__os}>'

    def set_os(self, new_os: str) -> None:
        self.__os = new_os

    def set_price(self, new_price: int) -> None:
        self.__price = new_price

    @property
    def year_made(self) -> int:
        return self.__made_in_year
