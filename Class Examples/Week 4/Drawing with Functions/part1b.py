"""
Here we've taken then simple first step of turning the bulk of our code into a single
function called main(). In many languages, main is the name of the function the provides the
"entry point" from the operating system for the running program. Another way to say it is
this is the first thing the program runs when you launch your Python code. While main is
a special name in some languages, in Python it is just convention for clarity. Let's do this
for the code below. First we "def"ine main as seen below. Then, at the bottom of the file
we "call" main. This is needed because a "define" does only that, it defines the function.
actually run it, we need to call it.

The last thing is some rather odd syntax at the bottom of the file:

if __name__ == "__main__":
    main()

Essentially, this is asking "is this file that is being used to launch the program" If "yes" then
run the main() function. Otherwise, don't.

This allows the main() function to run if the file is being run but not run if the file is being imported.
This is handy for files that contain utilities for import but may have some test code in main().

Of course, if you never intended to import the file as a library, then you can just put
main() to run the main function.

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
# Only run the main function if we are running this file. Don't run it
# if we are importing this file.
if __name__ == "__main__":
    main()
