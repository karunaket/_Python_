'''a, b = input("Enter the 1st and 2nd numbers: ").split()
sum = float(a) + float(b)
difference = float(a) - float(b)
product = float(a) * float(b)
division = float(a) / float(a)

print("sum: " + str(sum))
print("difference: " + str(difference))
print("product: " + str(product))
print("division: " + str(division))'''


'''price = 5
print(price > 10 or price < 30)'''


'''nickname = {"krishna":"chisna", "himanshu":"lawandi", "lalan":"dai"}

print(nickname.get("krishna"))
print(nickname.get("himanshu"))'''


'''item = 3

if item > 5:
    print("It's more than 5")
elif item == 3:
    print("It is 3")
else:
    print("There is no item")'''


'''a = input("Enter the number: ")
print(f"Multiplication table of {a} is:")
for i in range(1, 11):
    print(f"{int(a)} X {i} = {int(a)*i}")'''


'''my_string = "Hello, world!"
reversed_string = my_string[::-1]
print(reversed_string)'''


'''f = open('testfile.txt','r') # r (reading) mode is default
text = f.read()
print(text)
f.close()'''


'''f = open('testfile.txt','r')
text = f.read()
print(text)
f.close()'''

'''with open('testfile.txt', 'r') as f:
    text=f.read()
    print(text)'''


'''s1={1, 2, 5, 6}
s2={3, 6, 7}
print(s1.union(s2))
s1.update(s2)
print(s1, s2)'''