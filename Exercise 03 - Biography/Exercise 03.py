name = input("Enter your name: ")
hometown = input("Enter your hometown: ")
try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Invalid input! Please enter a number for age.")
    age = 0
biography = { "name": name, "hometown": hometown,"age": age }
print("Biography")
print("Name:", biography["name"])
print("Hometown:", biography["hometown"])
print("Age:", biography["age"])
