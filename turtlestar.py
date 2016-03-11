import turtle

# Ask user for input here.
n = raw_input("enter an odd natural number >= 5: ")
n = int(n)
while n < 5.0:
    n = raw_input("enter an odd natural number >= 5: ")
    n = int(n)
side_len = raw_input("Length of sides: ")
side_len = int(side_len)

# Now create a graphics window.
t = turtle.Pen()
for j in range (n):
    t.forward(side_len)
    t.left(1800/n)

# Put the rest of your code can go here

# Prevent the graphics window from diappearing too
# quickly to see it.
stopper = raw_input("Hit <enter> to quit.")

# Now remove the graphics window before exiting.
turtle.bye()
