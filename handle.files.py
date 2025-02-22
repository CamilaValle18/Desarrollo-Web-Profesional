try:
    path = 'C:\\DataFiles\\archivo.text'
    new_file = open(path, 'r')
    # data = new_file.readlines()
    # print(data)
    one_line = new_file.readline()
    one_line = new_file.readline()
    print(one_line)
    print(one_line)

    # for line in data:
        # print(line)

    # new_file = open('C:\\DataFiles\\archivo.text', 'w')
    # new_file.write("Hello world\n")
    # new_file.write("Hello mundo\n")
    # new_file.write("Hello UTVT\n")
    # new_file.close()
except Exception as e:
    print(e)