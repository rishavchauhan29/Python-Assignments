students = {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 90, "Eve": 88}

name = input("Enter the student's name: ")

if name in students:
    print(f"{name}'s marks: {students[name]}")
else:
    print(f"Student not found.")