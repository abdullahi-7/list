## List
# List is collection
# List is also named Collection , Array
# friends = ["Abdullahi", 10, True, "Khadija", 11, False]
# print(f"My frinds are {friends}")
# print("My friends are" , friends)
# print()

## how to manipulate a list
# friends = ["Abdi", "Salum", "Suheil", "Shueib"]
# print(friends)
# print(friends[0])
# print(friends[-1])

# friends[1] = "Hashim"
# print(friends)

# Exercise 1
# Write a list of school subject and print them

subject = ["math", "english", "kiswahili", "hygiene"]
print(f"subject of a school is {subject}")
print(subject)
print("\n")
# Exercise 2
# Write days of the week
days_of_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "friday"]
print(f"days of the week is {days_of_the_week}")
print(days_of_the_week)
print("")

# Print Index 3 and last index
print(days_of_the_week[2])
print(days_of_the_week[-1])
# change index 4 to the number of that day

days_of_the_week[3] = 4
print(days_of_the_week)


## Index()
print("Index number of Tuesday is: ",days_of_the_week.index("Tuesday"))
