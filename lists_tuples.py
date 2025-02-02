# --------------- Lists ---------------

# container to store a set of values of any data type
# mutable in nature unlike strings

my_list = ["apple", "shreya", False , 155.32 , 40, "orange", "rahul"]

# print(my_list)
# print(my_list[2])

my_list[2] = True
# print(my_list[2])

# slicing 
# print(my_list[2:5])

# methods / functions 
# (list changes when you run a method unlike strings)
# (strings return a new value when you run a method while here the existing list changes)

my_num = [22, 1,99,76,5,48]

my_num.sort()
# print(my_num)

my_num.reverse()
# print(my_num)

my_num.append(-1)

my_num.insert(3,32)
# print(my_num)

my_num.pop(1)  # takes index as agruement and also remove and return the value

my_num.remove(32)  # only removethe element


# --------------- Tuples ---------------

x = (1,3,"mango",5,7,"kiwi")
print(type(x))