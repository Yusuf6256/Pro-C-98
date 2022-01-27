def swapFile():
    text1 = input("Enter File Name: ")
    text2 = input("Enter File Name: ")
    
    with open(text1, "r") as a:
        data_a=a.read()

    with open(text2, "r") as a:
        data_b=a.read()

    with open(text1, "w") as a:
        a.write(data_b)

    with open(text2, "w") as a:
        a.write(data_a)

swapFile()