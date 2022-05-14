from gui_components.text_box import TextBox
from base.drawable_objects import GameObject
from gui_components.screen import Screen
from base.colors import *
from base.dimensions import Dimensions
from base.important_variables import *
from base.utility_functions import percentages_to_numbers
from base.velocity_calculator import VelocityCalculator

from gui_components.button import Button
from gui_components.grid import Grid
from gui_components.screen import Screen
from gui_components.t_chart import TChart
from gui_components.text_box import TextBox


class DocumentationScreen(Screen):
    """A Screen for displaying documentation for something"""

    documentation_name_field = None
    functions_and_description_table = None
    documentation_description_field = None
    components = []

    def __init__(self, documentation_name, documentation_description, functions_to_descriptions):
        """Initializes the object"""

        self.documentation_name_field = TextBox(documentation_name, 25, False, purple, white)
        self.documentation_description_field = TextBox(documentation_description, 16, False, dark_green, white)

        top_grid = Grid(Dimensions(0, 0, screen_length, screen_height * .1), None, 1, True)
        top_grid_components = [self.documentation_name_field, self.documentation_description_field]
        top_grid.turn_into_grid(top_grid_components, None, None)

        td = top_grid.dimensions
        buffer = screen_height * .02
        self.functions_and_description_table = TChart("Important Functions", "Description", functions_to_descriptions,
                                                      Dimensions(td.x_coordinate, td.bottom + buffer, screen_length, screen_height - td.height))

        self.components = top_grid_components + [self.functions_and_description_table]