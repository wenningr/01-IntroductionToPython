"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Greg Wenning.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################
import rosegraphics as rg

window = rg.SimpleTurtle('turtle')

blue_turtle = rg.SimpleTurtle('turtle')
blue_turtle.pen = rg.Pen('blue', 3)
blue_turtle.speed = 20

size = 150

for k in range(7):
    blue_turtle.draw_square(size)

    blue_turtle.pen_up()
    blue_turtle.left(45)
    blue_turtle.forward(10)
    blue_turtle.right(45)

    blue_turtle.pen_down()
    size = size - 12
red_turtle = rg.SimpleTurtle('turtle')
red_turtle.pen = rg.Pen('red', 3)
red_turtle.speed = 20

size = 150
for k in range(9):
    red_turtle.draw_square(size)

    red_turtle.pen_up()
    red_turtle.right(45)
    red_turtle.forward(10)
    red_turtle.left(45)

    red_turtle.pen_down()
    size = size - 12

