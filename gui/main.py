from gui.documentation_screen import DocumentationScreen
from gui_components.navigation_screen import NavigationScreen


class Main(NavigationScreen):
    """The main screen of the application"""

    def __init__(self):
        """Initializes the object"""

        sub_screens, names = self.get_names_and_screens()
        super().__init__(sub_screens, names)

    def get_window_documentation(self):
        function_to_description = {
            "run": "Happens every cycle. Goes through all the visible screens in 'screens' and for each visible component in screen.get_components() and 'components' it calls component.run() and component.render().",
            "add_screen": "Adds the screen to 'screens'",
            "add_component": "Adds the component to 'components'",
            "display_screens": "Makes the screen provided in the parameter visible and all other screens and components not visible",
            "display_components": "Makes the components provided in the parameter visible and all other screens and components not visible"
        }
        description = "Provides some utility functions that allows you from anywhere to modify what is displayed on the screen and to run code for components"
        return DocumentationScreen("Window", description, function_to_description)

    def get_component_documentation(self):
        function_to_description = {
            "run": "Must be implemented. The code for running everything that needs to be run for the component to work (besides making it appear on the screen). This code will be called every cycle if it is added to the window and is visible",
            "render": "Must be implemented. The code for making the component appear on the screen. This code will be called every cycle if it is added to the window and is visible"
        }

        description = "Everything that must be rendered and run has to implement this class. Provides a uniform way for things to be added to a window and still be able to be rendered and run"
        return DocumentationScreen("Component", description, function_to_description)

    def get_screen_documentation(self):
        function_to_description = {
            "run": "Must be implemented. The code for running everything that needs to be run in order for this screen to work",
            "get_components": "Returns the components that should be run and rendered. By default returns 'components,' but it can be changed"
        }

        description = "Everything that is made up of a composite of components should inherit from this. Think of it almost like a window in windows."
        return DocumentationScreen("Screen", description, function_to_description)

    def get_collisions_finder_documentation(self):
        function_to_description = {
            "is_collision": "If object1 and object2 have collided",
            "is_moving_collision": "If object1 and object2 have collided by moving into each other as opposed to just already being collided (within each other)",
            "is_right_collision": "If object1 has collided with object2's right edge by moving into it",
            "is_left_collision": "If object1 has collided with object2's left edge by moving into it",
            "is_top_collision": "If object1 has collided with object2's top by moving into it",
            "is_bottom_collision": "If object1 has collided with object2's bottom by moving into it",
            "get_objects_xy": "The object1's x and y coordinate when it collided with object2 (they must have collided)"
        }

        description = "Provides utility functions for figuring out if objects have collided and if so when and where"
        return DocumentationScreen("CollisionsFinder", description, function_to_description)

    def get_event_documentation(self):
        function_to_description = {
            "run": "Runs all the code for the event to work",
            "happened_last_cycle": "returns if the event happened last cycle",
            "is_conitnuous": "returns if the event happened last cycle and this cycle",
            "is_click": "returns if the event did not happen last cycle and happened this cycle"
        }

        description = "Provides an easy way to see if an event happened in the past and stuff of that sort"
        return DocumentationScreen("Event", description, function_to_description)

    def get_timed_event_description(self):
        function_to_description = {
            "run": "Runs all the code for figuring out if the event is done and if it has to be reset",
            "start": "Starts the timer for the event",
            "reset": "Stops the timer for the event and makes it 0",
            "is_done": "returns if the timed event is done"
        }

        description = "Provides an easy way for timing things like for instance a short press is a small jump and a long press is a big jump"
        return DocumentationScreen("Timed Event", description, function_to_description)

    def get_history_keeper_description(self):
        function_to_description = {
            "add": "Adds the object to the history keeper so it can keep an example of it (give it a unique name) from the past. Stores the cycle from which is what added from, so it can find the object from the last cycle when 'get_last' is called",
            "get_last": "Gets the object from the last cycle using the unique name given in 'add'"
        }

        description = "Provides a way to see what happened in the past making collisions and other things possible"
        return DocumentationScreen("History Keeper", description, function_to_description)

    def get_physics_equation_description(self):
        function_to_description = {
            "get_time_to_vertex": "returns the time it takes to reach the vertex",
            "set_acceleration": "sets the acceleration of the physics equation using the time and displacement",
            "set_velocity": "sets the velocity of the physics equation from the vertex and time",
            "set_variables": "sets the variables based on what is passed by the **kwargs",
            "get_distance": "returns the distance (or more specifically the y coordinate) at that time",
            "get_velocity_using_time": "returns the velocity at that specified time",
            "get_velocity_using_displacement": "returns the velocity using displacement (how much distance has been displaced from its start position)"
        }

        description = "Provides an easy way to model stuff in the real world like slowing down a stop or parabolic jumping"
        return DocumentationScreen("Physics Equation", description, function_to_description)

    def get_other_stuff(self):
        file_to_description = {
            "dimensions.py": "Provides an easy way to store the x, y, length, and height of an object. Also provides stuff like right_edge and bottom which are calculated from the x, y, length, and height",
            "game_object.py": "Provides a way for a rectangular object to have the render method already done as long as its dimensions are set",
            "important_variables.py": "Stores all the important variables like the window, window dimensions, etc)",
            "colors.py": "Has a bunch of colors; very helpful for making good looking GUI's",
            "velocity_calculator.py": "Is the way to find the time of the last cycle and get the distance traveled by giving the object's velocity",
            "path.py": "Provides ways for things to follow a path; very good for AI's. If you want to work on this type of stuff just ask me to go more in depth",
            "intermediate_screens.py": "Provides a way to have a screen that appears for a short amount of time",
            "selection_screen.py": "Provides a way to have a screen which allows you to go to other screens easily",
        }

        description = "Other important stuff that I didn't feel like needed a ton of elaboration, but if you feel like it does just ask me"
        return DocumentationScreen("Other Stuff", description, file_to_description)

    def get_names_and_screens(self):
        """returns: List[2]; [documentation screens, names]"""

        documentation_screens = [self.get_window_documentation(), self.get_component_documentation(), self.get_screen_documentation(), self.get_collisions_finder_documentation(), self.get_event_documentation(), self.get_timed_event_description(), self.get_history_keeper_description(), self.get_physics_equation_description(), self.get_other_stuff()]
        names = []

        for screen in documentation_screens:
            names.append(screen.documentation_name_field.text)

        return [documentation_screens, names]

