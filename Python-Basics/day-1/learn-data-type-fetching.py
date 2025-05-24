
# to fetch data type of variable use -> type()

age=24
type_age = type(age)

height=5.7
type_height = type(height)

name="ketan"
type_name = type(name)

isReadyToLearnPython = True
type_isReadyToLearnPython = type(isReadyToLearnPython)


fruits = ["apple", "banana", "cherry"]
type_fruits = type(fruits)


coordinates = (10, 20)
type_coordinates=type(coordinates)

unique_numbers = {1, 2, 3, 2, 1}
type_unique_numbers = type(unique_numbers)

student = {
    name: "Ketan",
    "name":"Vilas",
    "age": 24,
    "isEnrolled": True
}
type_student = type(student)

print(type_age)
print(type_height)
print(type_name)
print(type_fruits)
print(type_coordinates)
print(type_unique_numbers)
print(type_student)
