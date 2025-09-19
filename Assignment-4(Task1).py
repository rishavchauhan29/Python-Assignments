try:

    file = open("F:\Python-Course\Assignment-4\sample.txt", "r")
    reading_file = file.read()
    print(reading_file)

except FileNotFoundError:
    print(f"Error: The file \"sample.txt\" was not found.")

    file.close()
