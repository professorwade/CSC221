"""
Moving the grass drawing code went well, let's do it again for the snow person code. Below,
we've moved the code for drawing the snow person into a separate function and replaced where it
was with a function call to the new function. Now our main function is looking much simpler
than before, and we can readily read it and discern what the code is doing. While we're here
I want to demonstrate an IDE feature called code-folding where we can hide blocks of code
to make it easier to show only the code we are interested in on the screen. Just hover the mouse
to the left of the function definition and click on the down arrow. Notice that the code in that
function is "folded up" under the definition.

Now, suppose we wanted to draw multiple snow persons in different places. We can just call
the function multiple times because each time the same graphics will be drawn in the same
location on the screen. How to solve? Parameter passing.
"""

import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

def draw_grass():
    """ Draw the ground """
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.AIR_SUPERIORITY_BLUE)


def draw_snow_person():
    """ Draw a snow person """

    # Snow
    arcade.draw_circle_filled(300, 200, 60, arcade.color.WHITE)
    arcade.draw_circle_filled(300, 280, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(300, 340, 40, arcade.color.WHITE)

    # Eyes
    arcade.draw_circle_filled(285, 350, 5, arcade.color.BLACK)
    arcade.draw_circle_filled(315, 350, 5, arcade.color.BLACK)


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.DARK_BLUE)
    arcade.start_render()

    draw_grass()
    draw_snow_person()

    # Finish and run
    arcade.finish_render()
    arcade.run()


# Call the main function to get the program started.
main()