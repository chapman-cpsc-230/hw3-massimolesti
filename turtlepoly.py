import turtle
# Ask user for input here.
num_sides = raw_input("Number of sides: ")
num_sides = int(num_sides)
side_len = raw_input("Length of sides: ")
side_len = int(side_len)
# Now create a graphics window.
t = turtle.Pen()
for j in range (num_sides):
    t.left(360.0/num_sides)
    t.forward(side_len)
# Put the rest of your code can go here

# Prevent the graphics window from diappearing too
# quickly to see it.
stopper = raw_input("Hit <enter> to quit.")

# Now remove the graphics window before exiting.
turtle.bye()
