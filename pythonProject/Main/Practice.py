print("This is a Practice Project")






#defining variables
x = 3
y = 3.0
z = 'Test'

print(x, y, z)

print(type(x), type(y), type(z))

#to identify the type of variable
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

#Assign multiple values in the same line
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#one value to many
x = y = z = "Orange"

print(x,y,z)


#Unpack a list/tuple

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)



import random
#generate a random number betwen 1 to 10
print(random.randrange(1, 10))


#If you use the global keyword, the variable belongs to the global scope:

x = 'test'

def myfunc():
#  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

print('test')

