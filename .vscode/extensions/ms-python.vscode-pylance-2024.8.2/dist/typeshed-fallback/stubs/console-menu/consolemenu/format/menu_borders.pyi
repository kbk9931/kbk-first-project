import logging

class MenuBorderStyle:
    @property
    def bottom_left_corner(self) -> str: ...
    @property
    def bottom_right_corner(self) -> str: ...
    @property
    def inner_horizontal(self) -> str: ...
    @property
    def inner_vertical(self) -> str: ...
    @property
    def intersection(self) -> str: ...
    @property
    def outer_horizontal(self) -> str: ...
    @property
    def outer_horizontal_inner_down(self) -> str: ...
    @property
    def outer_horizontal_inner_up(self) -> str: ...
    @property
    def outer_vertical(self) -> str: ...
    @property
    def outer_vertical_inner_left(self) -> str: ...
    @property
    def outer_vertical_inner_right(self) -> str: ...
    @property
    def top_left_corner(self) -> str: ...
    @property
    def top_right_corner(self) -> str: ...

class AsciiBorderStyle(MenuBorderStyle):
    @property
    def bottom_left_corner(self) -> str: ...
    @property
    def bottom_right_corner(self) -> str: ...
    @property
    def inner_horizontal(self) -> str: ...
    @property
    def inner_vertical(self) -> str: ...
    @property
    def intersection(self) -> str: ...
    @property
    def outer_horizontal(self) -> str: ...
    @property
    def outer_horizontal_inner_down(self) -> str: ...
    @property
    def outer_horizontal_inner_up(self) -> str: ...
    @property
    def outer_vertical(self) -> str: ...
    @property
    def outer_vertical_inner_left(self) -> str: ...
    @property
    def outer_vertical_inner_right(self) -> str: ...
    @property
    def top_left_corner(self) -> str: ...
    @property
    def top_right_corner(self) -> str: ...

class LightBorderStyle(MenuBorderStyle):
    @property
    def bottom_left_corner(self) -> str: ...
    @property
    def bottom_right_corner(self) -> str: ...
    @property
    def inner_horizontal(self) -> str: ...
    @property
    def inner_vertical(self) -> str: ...
    @property
    def intersection(self) -> str: ...
    @property
    def outer_horizontal(self) -> str: ...
    @property
    def outer_horizontal_inner_down(self) -> str: ...
    @property
    def outer_horizontal_inner_up(self) -> str: ...
    @property
    def outer_vertical(self) -> str: ...
    @property
    def outer_vertical_inner_left(self) -> str: ...
    @property
    def outer_vertical_inner_right(self) -> str: ...
    @property
    def top_left_corner(self) -> str: ...
    @property
    def top_right_corner(self) -> str: ...

class HeavyBorderStyle(MenuBorderStyle):
    @property
    def bottom_left_corner(self) -> str: ...
    @property
    def bottom_right_corner(self) -> str: ...
    @property
    def inner_horizontal(self) -> str: ...
    @property
    def inner_vertical(self) -> str: ...
    @property
    def intersection(self) -> str: ...
    @property
    def outer_horizontal(self) -> str: ...
    @property
    def outer_horizontal_inner_down(self) -> str: ...
    @property
    def outer_horizontal_inner_up(self) -> str: ...
    @property
    def outer_vertical(self) -> str: ...
    @property
    def outer_vertical_inner_left(self) -> str: ...
    @property
    def outer_vertical_inner_right(self) -> str: ...
    @property
    def top_left_corner(self) -> str: ...
    @property
    def top_right_corner(self) -> str: ...

class HeavyOuterLightInnerBorderStyle(HeavyBorderStyle):
    @property
    def inner_horizontal(self) -> str: ...
    @property
    def inner_vertical(self) -> str: ...
    @property
    def intersection(self) -> str: ...
    @property
    def outer_horizontal_inner_down(self) -> str: ...
    @property
    def outer_horizontal_inner_up(self) -> str: ...
    @property
    def outer_vertical_inner_left(self) -> str: ...
    @property
    def outer_vertical_inner_right(self) -> str: ...

class DoubleLineBorderStyle(MenuBorderStyle):
    @property
    def bottom_left_corner(self) -> str: ...
    @property
    def bottom_right_corner(self) -> str: ...
    @property
    def inner_horizontal(self) -> str: ...
    @property
    def inner_vertical(self) -> str: ...
    @property
    def intersection(self) -> str: ...
    @property
    def outer_horizontal(self) -> str: ...
    @property
    def outer_horizontal_inner_down(self) -> str: ...
    @property
    def outer_horizontal_inner_up(self) -> str: ...
    @property
    def outer_vertical(self) -> str: ...
    @property
    def outer_vertical_inner_left(self) -> str: ...
    @property
    def outer_vertical_inner_right(self) -> str: ...
    @property
    def top_left_corner(self) -> str: ...
    @property
    def top_right_corner(self) -> str: ...

class DoubleLineOuterLightInnerBorderStyle(DoubleLineBorderStyle):
    @property
    def inner_horizontal(self) -> str: ...
    @property
    def inner_vertical(self) -> str: ...
    @property
    def intersection(self) -> str: ...
    @property
    def outer_horizontal_inner_down(self) -> str: ...
    @property
    def outer_horizontal_inner_up(self) -> str: ...
    @property
    def outer_vertical_inner_left(self) -> str: ...
    @property
    def outer_vertical_inner_right(self) -> str: ...

class MenuBorderStyleType:
    ASCII_BORDER: int
    LIGHT_BORDER: int
    HEAVY_BORDER: int
    DOUBLE_LINE_BORDER: int
    HEAVY_OUTER_LIGHT_INNER_BORDER: int
    DOUBLE_LINE_OUTER_LIGHT_INNER_BORDER: int

class MenuBorderStyleFactory:
    logger: logging.Logger
    def __init__(self) -> None: ...
    def create_border(self, border_style_type: MenuBorderStyleType) -> MenuBorderStyle: ...
    def create_ascii_border(self) -> AsciiBorderStyle: ...
    def create_light_border(self) -> LightBorderStyle: ...
    def create_heavy_border(self) -> HeavyBorderStyle: ...
    def create_heavy_outer_light_inner_border(self) -> HeavyOuterLightInnerBorderStyle: ...
    def create_doubleline_border(self) -> DoubleLineBorderStyle: ...
    def create_doubleline_outer_light_inner_border(self) -> DoubleLineOuterLightInnerBorderStyle: ...
    @staticmethod
    def is_win_python35_or_earlier() -> bool: ...
