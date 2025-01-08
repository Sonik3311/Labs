def read_file(filename, read_whole: bool):
    try:
        with open(filename, "r") as file:
            contents = ""
            if read_whole:
                contents = file.read()
            else:
                for line in file:
                    contents += line
            return contents
    except FileNotFoundError:
        print(f"Couldn't read {filename} (file not found)")



print(read_file("example.txt", False))