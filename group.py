

test_list = [2, 4, 6, 8, 10, 6, 7, 4, 9]
#Takes in a list of integers, and splits it into sub-lists of length 3 each
# if there are not enough values to fill the last list, submits a shorter list then
def groups_of_3(input_list:list[int]) -> list[list[int]]:
    output_list = []
    for i in range(0, len(input_list), 3):
        temp_list = []
        for j in range(i, i+3):
            if j in range(0, len(input_list)):
                temp_list.append(input_list[j])
        output_list.append(temp_list)
    return output_list

print(groups_of_3(test_list))

