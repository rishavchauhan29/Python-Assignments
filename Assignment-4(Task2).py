input1 = input("Enter some text: ")
with open("F:\Python-Course\Assignment-4\output.txt", "w") as file:
    file.write(input1 + "\n")


input2 = input("Enter more text to append: ")
with open("F:\Python-Course\Assignment-4\output.txt", "a") as file:
    file.write(input2 + "\n")

with open("F:\Python-Course\Assignment-4\output.txt", "r") as file:
    reading_file = file.read()
    print("\nFinal file content: ")
    print(reading_file)