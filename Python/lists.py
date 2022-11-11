# Lists are used to store multiple values in single variable
nums = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(nums)

# We can also store different types of data in one list
data = [1, 2.3, 10, "Vamstar", True]
print(data)

# We can access list by index number
print(data[0])
print(data[3])
print(fruits[2:5])
print(fruits[-1])
print(fruits[3:])
print(fruits[:3])

# We can update elements in list
print(data[-1])
data[-1] = False
print(data[-1])

# We can insert elements into list
data.insert(1, "Code")
print(data)