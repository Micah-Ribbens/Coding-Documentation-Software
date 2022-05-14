from base.dimensions import Dimensions
from gui_components.component import Component
from base.drawable_objects import GameObject
from base.colors import *
from base.important_variables import *
from gui_components.grid import Grid

from gui_components.text_box import TextBox


class TChart(Component):
    """A way of displaying data in a T-Chart format"""

    components = []

    def __init__(self, left_title, right_title, left_to_right_values: dict, dimensions):
        """Initializes the object"""

        dividing_line_length = 10
        self.set_dimensions(dimensions)

        left_title_field = TextBox(left_title, 20, False, white, blue)
        right_title_field = TextBox(right_title, 20, False, white, purple)

        left_title_field.number_set_dimensions(self.x_coordinate, self.y_coordinate, (self.length - dividing_line_length) / 2, self.height * .1)
        right_title_field.number_set_dimensions(left_title_field.right_edge + dividing_line_length, self.y_coordinate, left_title_field.length, left_title_field.height)
        dividing_line = GameObject(left_title_field.right_edge, left_title_field.y_coordinate, screen_height, dividing_line_length, black)
        top_line = GameObject(self.x_coordinate, left_title_field.bottom, dividing_line_length, self.length, black)

        self.components = [left_title_field, right_title_field]

        left_value_fields = []
        for left_value in left_to_right_values.keys():
            left_value_field = TextBox(left_value, 16, False, white, left_title_field.background_color)
            left_value_fields.append(left_value_field)

        right_value_fields = []
        for right_value in left_to_right_values.values():
            right_value_field = TextBox(right_value, 16, False, white, right_title_field.background_color)
            right_value_field.set_text_is_centered(False)
            right_value_fields.append(right_value_field)

        grid = Grid(Dimensions(left_title_field.x_coordinate, top_line.bottom,
                                left_title_field.length - dividing_line_length, self.height - left_title_field.height), 1, None, True)
        grid.turn_into_grid(left_value_fields, None, None)

        grid = Grid(Dimensions(dividing_line.right_edge, top_line.bottom,
                                right_title_field.length, self.height - right_title_field.height), 1, None, True)
        grid.turn_into_grid(right_value_fields, None, None)

        self.components += (left_value_fields + right_value_fields)

        # So it can draw over the lines in case of any mistakes
        self.components += [dividing_line, top_line]

    def render(self):
        for component in self.components:
            component.render()

    def run(self):
        pass