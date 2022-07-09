from codecs import charmap_build
import string


x="awesome"  #x is a global variable
def myfunc():
    print("python is "+x)

myfunc()

#If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. 
#The global variable with the same name will remain as it was, global and with the original value.

def myfunc2():
    x="fantastic" # x is a local variable.
    print("python is "+x)

myfunc2()

#To create a global variable inside a function, you can use the global keyword.
def myfunc3():
    global T  # its declaration
    T=4.5
    print(T)

myfunc3()
print(T)

#To change the value of a global variable inside a function, refer to the variable by using the global keyword:
def myfunc4():
    global x
    x="fantastic"
    print(x)
myfunc4()
print(x)
