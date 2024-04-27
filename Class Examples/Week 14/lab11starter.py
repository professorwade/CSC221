"""
Array Backed Grid

Show how to use a two-dimensional list/array to back the display of a
grid on-screen.

Steps:
Part 1:
   Modify the starting code (see lab description) to toggle the color (white/green) of the square clicked and
   the squares above, below, right, and left. I.e. if nothing is green, clicking on a square
   should result in five squares turning green. Subsequent clicks on other squares will toggle
   the color of the squares depending on what they are when clicked. See lab description.
    * in order to do this, you will need to check the validity of the square before attempting
       to change its value. For example, if you click on the upper right square, the square to the
       left and below can be toggled (in addition to the one clicked) but attempting to toggle outside
       the grid is not possible. Attempting to do so will cause an error in accessing the grid dimensions.

Part 2:
   1. Create a second Python program (starting with the starting code)
   2. Write a loop that will count all of the cells that are selected in the grid and print them out. Put
      this code at the end of your on_mouse_press function. (See lab description for example)
   3. Write another loop that will print how many cells are selected in each row (See lab description for example)
   4. Update the code so that it prints the count in both rows and columns(See lab description for example)
   5. Update the code so that the program will also print how many cells are continuously (with no skips)
      selected in a row, if that number is greater than 2.

"""
import arcade

# Set how many rows and columns we will have
# these are the dimensions of our grid representation
ROW_COUNT = 10
COLUMN_COUNT = 10

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 20
HEIGHT = 20

# This sets the margin between each cell
# and on the edges of the screen.
MARGIN = 5

# Do the math to figure out our screen dimensions
SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN

class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height):
        """
        Set up the application.
        """
        super().__init__(width, height)
        # Create a two-dimensional array. A two-dimensional
        # array is simply a list of lists.
        self.grid = [] # create an empty list
        for row in range(ROW_COUNT):
            # Add an empty array that will hold each cell
            # in this row
            self.grid.append([]) # append a new empty list to the list element
            for column in range(COLUMN_COUNT):
                self.grid[row].append(0)  # Append a cell (iterate across columns for each row)

        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw the grid
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                # Figure out what color to draw the box
                if self.grid[row][column] == 1:
                    color = arcade.color.GREEN
                else:
                    color = arcade.color.WHITE

                # Do the math to figure out where the box is
                x = (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2
                y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2

                # Draw the box
                arcade.draw_rectangle_filled(x, y, WIDTH, HEIGHT, color)

    # this is called each time a mouse button is pressed
    # in this case we don't really care which button was pressed, but we do want the coordinates in x and y
    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called when the user presses a mouse button.
        """

        # Change the x/y screen coordinates to grid coordinates
        column = x // (WIDTH + MARGIN)
        row = y // (HEIGHT + MARGIN)

        print(f"Click Screen coordinates: ({x}, {y}). Grid coordinates: ({row}, {column})")

        # Make sure we are on-grid. It is possible to click in the upper right
        # corner in the margin and go to a grid location that doesn't exist
        if row < ROW_COUNT and column < COLUMN_COUNT:

            # Flip the location between 1 and 0.
            if self.grid[row][column] == 0:
                self.grid[row][column] = 1
            else:
                self.grid[row][column] = 0


def main():

    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()


if __name__ == "__main__":
    main()