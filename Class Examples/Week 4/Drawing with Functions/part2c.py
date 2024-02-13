"""
With functions, you can pass in additional information to the function to refine what it does.
Here is a simple example where we are going to pass in an x and y coordinate instructing the
draw_snow_person function where to draw. It will use the x and y coordinate as a starting
point for all the drawing functions.

Using this mechanism, we can draw snow persons all over the place and all we have to do is pass
in a different x and y! As far as the syntax, it's pretty simple, just put the values in the
same order as you take them out. I.e. if you do 100, 50 in the function call then a function
defined as def func(x, y) will have a value of x = 100 and y = 50 in the func() function.

I do need to point something out here, not to overly complicate things but the clarification will
help down the road. You don't have to name the variables the same thing in the function call
as the function definition. I.e. if you have variables x and y in the call, you can have a and b
in the function definition. The variable names are just a placeholder and what you name them
have no effect on the calling function. Position is important, not name.

For example, if the calling function is func(a, b) and the definition is func(x, y), in func, x
will have a value of a and y will have a value of b.

Another thing to point out is this type of parameter passing is called "pass-by-value" in which
a copy of the value passed to the function is used. What this means is that if the called function
changes that value, those changes are lost when the function returns.

If you need a modified value, the called function can return it (with the return keyword) or you
can pass it by a reference which we'll get into later.
"""

import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def draw_grass():
    """ Draw the ground """
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.AIR_SUPERIORITY_BLUE)


def draw_snow_person(x, y):
    """ Draw a snow person """

    # Draw a point at x, y for reference
    arcade.draw_point(x, y, arcade.color.RED, 5)

    # Snow
    arcade.draw_circle_filled(300 + x, 200 + y, 60, arcade.color.WHITE)
    arcade.draw_circle_filled(300 + x, 280 + y, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(300 + x, 340 + y, 40, arcade.color.WHITE)

    # Eyes
    arcade.draw_circle_filled(285 + x, 350 + y, 5, arcade.color.BLACK)
    arcade.draw_circle_filled(315 + x, 350 + y, 5, arcade.color.BLACK)



def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.DARK_BLUE)
    arcade.start_render()

    draw_grass()
    draw_snow_person(50, 50)


    # Finish and run
    arcade.finish_render()
    arcade.run()


# Call the main function to get the program started.
main()