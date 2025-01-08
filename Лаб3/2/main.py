def write_to(filename, data):
    try:
        with open(filename, "a") as f:
            f.write("\n" + data)
    except FileNotFoundError:
        with open(filename, "w") as f:
            f.write(data)

user_input = str(input("Введите текст: "))
write_to("user_input.txt", user_input)