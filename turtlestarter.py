import turtle
def draw_reg_polygon(t,num_sides,side_len):
    t.left(30)
    for i in range(num_sides):
        t.forward(side_len)
        t.left(360.0/num_sides)
# Ask user for input here.

# Now create a graphics window.
t = turtle.Pen()
for j in range (3):
    draw_reg_polygon(t,6,50)
    t.right(150)
# Put the rest of your code can go here

# Prevent the graphics window from diappearing too
# quickly to see it.
stopper = raw_input("Hit <enter> to quit.")

# Now remove the graphics window before exiting.
turtle.bye()
