import os

if __name__ == '__main__':
    print("Welcome")

    while True:
        x = input("ENTER WHAT YOU WANT TO SPEAK: ")
        if x == 'z':
            os.system("Say Bye, see you")
            break
        command = f"say {x}"
        os.system(command)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
