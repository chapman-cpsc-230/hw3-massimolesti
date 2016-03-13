from math import sqrt
for n in range (1,60):
    r = 2.0
    for i in range (n):
        r = sqrt(r)
    for i in range (n):
        r = r**2
    print '%d times sqrt and **2: %.16f' %(n,r)
#This program is taking the number designated in r and first taking the square root of the number, and then squaring that square root
for n in range (1,60):
    r = 2.0
    for i in range (n):
        r1 = sqrt(r)
    for i in range (n):
        r2 = r1**2
        r = r2
        while i == 51:
            print "The square root of 2.0 equals %.16f; that number squared is %.16f" %(r1,r2)
            n.remove (51)
#The square root of 2 is an infinite decimal and the computer cannot save an infinite amount of numbers. So, it rounds instead. However, when that number is called to be squared, the rounded version is used which means it won't actually be 2.0 again. done enough times, the proces will drastically change the outcomes. 

### MAM: Lines of code (including comments should be short 
### -- no more than 80 characters.
### Your comments should be broken up into multiple lines.
