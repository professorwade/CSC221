import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# replace with Car
class Box:
    def __init__(self, position_x, position_y, width, height, color):
        self.position_x = position_x
        self.position_y = position_y
        self.width = width
        self.height = height
        self.color = color

    def draw(self):
        # draw the box (your code to draw the car goes here)
        # note that the car should use self.position_x and y so that its position with move
        # with mouse
        arcade.draw_rectangle_filled(self.position_x,
                                     self.position_y,
                                     self.width,
                                     self.height,
                                     self.color)

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        # Call the parent class's init function
        super().__init__(width, height, title)

        # only need to call this once
        self.set_mouse_visible(False)

        # draw the background
        arcade.set_background_color(arcade.color.AVOCADO)

        # Create the box (you'll create your car instance here by calling the car constructor
        # instead of the box
        self.box = Box(100, 100, 50, 50, arcade.color.BLUE)

    def on_mouse_motion(self, x, y, dx, dy):
        # update the position by setting the box instance variable coordinates based
        # on the mouse coordinates
        self.box.position_x = x
        self.box.position_y = y

    def on_draw(self):
        arcade.start_render()

        # draw the stands
        arcade.draw_rectangle_filled(400, 500, 300, 130, arcade.color.ALICE_BLUE)
        # draw the stands
        arcade.draw_line(250, 510, 550, 510, arcade.color.ARSENIC, 2)
        arcade.draw_line(250, 530, 550, 530, arcade.color.ARSENIC, 2)
        arcade.draw_line(250, 550, 550, 550, arcade.color.ARSENIC, 2)
        # draw the track
        arcade.draw_ellipse_outline(400, 300, 650, 400, arcade.color.ARSENIC, 65)
        arcade.draw_ellipse_outline(400, 300, 600, 340, arcade.color.ALICE_BLUE, 2)
        # draw the car
        # the position gets updated in the mouse position event handler then the drawing updated here
        self.box.draw()

def main():
    window = MyGame(800, 600, "Box")
    arcade.run()


main()