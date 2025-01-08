def read_file(read_whole: bool):
    with open("example.txt", "r") as file:
        contents = ""
        if read_whole:
            contents = file.read()
        else:
            for line in file:
                contents += line
        return contents

print(read_file(False))
