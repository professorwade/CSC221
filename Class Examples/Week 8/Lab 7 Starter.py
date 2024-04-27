""" Lab 7 - User Control """

import arcade
import random

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Box:
    def __init__(self, position_x, position_y, size, color):
        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.size = size
        self.color = color
        self.angle = 0

    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_rectangle_outline(self.position_x, self.position_y, self.size, self.size, self.color, 10, self.angle)

class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")
        self.box = Box(400, 300, 50, arcade.color.RADICAL_RED)
        self.target_x = 0
        self.target_y = 0
        self.increment = 1
        self.explosion_sound = arcade.load_sound("../Week 10/explosion.wav")
        self.explosion_sound_player = None

    def on_draw(self):
        arcade.start_render()
        self.box.draw()

        self.box.angle += 4 % 360

        self.box.size += self.increment

        if self.box.size < 10 : self.increment = 1

        if self.box.size > 100 : self.increment = -1

        # update x coord
        if self.box.position_x < self.target_x:
            self.box.position_x += 1

        elif self.box.position_x > self.target_x:
            self.box.position_x -= 1

        # update y coord
        if self.box.position_y < self.target_y:
            self.box.position_y += 1

        elif self.box.position_y > self.target_y:
            self.box.position_y -= 1

    def on_key_press(self, symbol: int, modifiers: int):
        self.box.color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.target_x = x
            self.target_y = y
        if button == arcade.MOUSE_BUTTON_RIGHT:
            if not self.explosion_sound_player or not self.explosion_sound_player.playing:
                self.explosion_sound_player = arcade.play_sound(self.explosion_sound)

def main():
    window = MyGame()
    arcade.run()


main()