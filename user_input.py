from image_to_text import *
def input_func():
    print("Hello User!"
          "Enter 1 for image, 2 for text")
    configs = int(input("Enter: "))

    if configs == 1:
        return image_to_text(input("Enter the path to the image: "))
    elif configs == 2:
        return input("Enter the text: ")
    else:
        print("wrong input, enter 1 for image or 2 for text")
        input_func()

