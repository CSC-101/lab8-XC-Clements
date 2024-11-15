import sys
#Tries to convert a value into a float
def convert_to_float(input_str:str):
    try:
        return float(input_str)
    except ValueError as e:
        print(e)
        return None


#Tries opening the provided file in the arguments
def can_opener():
    try:
        input_arg = sys.argv[1]
        input_file = open(input_arg, "r")
    except IndexError:
        return "error: no argument provided"
    except FileNotFoundError:
        return "error: file not found"
#Reads each line, if the line is 2 objects and each is a float adds them, otherwise prints errors
    for line in input_file:
        char_list = line.split()
        if len(char_list) == 2:
            if convert_to_float(char_list[0]) is not None and convert_to_float(char_list[1]) is not None:
                print(str(convert_to_float(char_list[0]) + convert_to_float(char_list[1])))
            else:
                print("values given are not the correct format")
        else:
            print("line is not the correct length")


    input_file.close()



if __name__ == '__main__':
    can_opener()