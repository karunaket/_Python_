#append()



numbers = [1, 2, 3, 4, 5]

#To add a new elemnent at the end of this list, we can use append method

numbers.append(6) 
print(numbers)



#insert()



numbers2 = [1, 2, 3, 4, 5]

#To insert a number at the middle or beginning of the list

numbers2.insert(0, -1)
#Here, 0 is the index and -1 is the number to insert...So this will insert -1 before the index 0

#After this the OUTPUT : [-1, 1, 2, 3, 4, 5, 6]

numbers2.insert(2, "Heyy")
#Here, 2 is the index and "Heyy" is the string to insert...So this will insert "Heyy" before the index 2
print(numbers2)



#remove()



nums = [23, 34, 56, 78]

nums.remove(56)
#It removes the no. 56 from the list
print(nums)



#clear()



nums2 = [243, 534, 856, 978]

nums2.clear()
#It removes all the nos. from the list
print(nums2)



#To check whether the give no. is in the list or not:



apple = [1, 2, 3, 4, 5]
print(2 in apple)       # 2 is the no. and apple is the name of the list



#len



apple = [1, 2, 3, 4, 5]
print(len(apple))       # It returns the no. of elements in the list named apple

test = "Nakib gajfukka"
print(len(test))        # It returns the no. of elements in the variable named test