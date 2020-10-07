import abc
from typing import List

class DrawableItem(abc.ABC):

    @abc.abstractmethod
    def draw(self) -> None:
        ...

class Triangle(DrawableItem):

    def draw_triangle(self) -> None:
        print(f'{type(self).__name__}: Drawing a triangle...')

    def draw(self) -> None:
        self.draw_triangle()

class BlackHole(DrawableItem):

    def draw_black_hole(self) -> None:
        print(f'{type(self).__name__}: Drawing a black hole...')

    def draw(self) -> None:
        self.draw_black_hole()


class ElonMusk(DrawableItem):
    
    def draw_elon_musk(self) -> None:
        print(f'{type(self).__name__}: Blimey!! Drawing Elon Musk...')

    def draw(self) -> None:
        self.draw_elon_musk()

drawable_items : List[DrawableItem] = [Triangle(), BlackHole(), ElonMusk()]

for drawable_item in drawable_items:
    drawable_item.draw()