# The Python print() function is often used to output variables.
x="john"
print(x)

#In the print() function, you output multiple variables, separated by a comma:

a="john"
b="rahul"
c="lol"
print(a,b,c)

# You can also use the + operator to output multiple variables: String Concatenation
print(a+b+c)

#In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error:
"""A="john"
B=5
print(A+B)"""

#The best way to output multiple variables in the print() function is to separate them with commas, which even support different data types:
A="john"
B=5
print(A,B)