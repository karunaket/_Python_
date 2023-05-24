''' Taking one input at a time '''

name = input("Wat is your name? ")

'''
int(input(...)) --> Taking integer as an input
float(input(...)) --> Taking float as an input
bool(input(...)) --> Taking boolean as an input
input(...) --> If nothing is specified then it will take it as string

'''

print("Hello " + name)

''' Taking multiple input at a time '''

x, y = input("Enter the name and age: ").split()

print(x)
print(y)