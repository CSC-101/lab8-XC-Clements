import sys

def convert_to_float(input_str:str):
    try:
        return float(input_str)
    except:
        return None



def can_opener():
    try:
        input_arg = sys.argv[1]
        input_file = open(input_arg, "r")
    except IndexError:
        return "error: no argument provided"
    except FileNotFoundError:
        return "error: file not found"
    final_output_list = []
    for line in input_file:
        output = None
        temp_output_list = []
        char_list = line.split()
        if len(char_list) == 2:
            if convert_to_float(char_list[0]) and convert_to_float(char_list[1]):
                print(str(convert_to_float(char_list[0]) + convert_to_float(char_list[1])))
            else:
                print("values given are not the correct format")
        else:
            print("line is not the correct length")


    input_file.close()



if __name__ == '__main__':
    can_opener()