"""
Here we've taken then simple first step of turning the bulk of our code into a single
function called main(). In many languages, main is the name of the function the provides the
"entry point" from the operating system for the running program. Another way to say it is
this is the first thing the program runs when you launch your Python code. While main is
a special name in some languages, in Python it is just convention for clarity. Let's do this
for the code below. First we "def"ine main as seen below. Then, at the bottom of the file
we "call" main. This is needed because a "define" does only that, it defines the function.
actually run it, we need to call it.
"""

import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.DARK_BLUE)
    arcade.start_render()

    # Draw the ground
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.AIR_SUPERIORITY_BLUE)

    # Draw a snow person

    # Snow
    arcade.draw_circle_filled(300, 200, 60, arcade.color.WHITE)
    arcade.draw_circle_filled(300, 280, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(300, 340, 40, arcade.color.WHITE)

    # Eyes
    arcade.draw_circle_filled(285, 350, 5, arcade.color.BLACK)
    arcade.draw_circle_filled(315, 350, 5, arcade.color.BLACK)

    # Finish and run
    arcade.finish_render()
    arcade.run()


# Call the main function to get the program started.
main()