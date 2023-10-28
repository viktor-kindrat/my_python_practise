try:
    with open("files/calculate.txt", "r") as readText:
        try:
            num = int(readText.read()) + 1
        except ValueError:
            num = 1

    with open("files/calculate.txt", "w") as writeText:
        writeText.write(str(num))
        print("\nIteration written, count of iteration is", num, sep=": ", end="\n\n")
except IOError:
    print("An error occurred while reading or writing the file.")
