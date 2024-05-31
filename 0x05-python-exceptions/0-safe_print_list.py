#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    index = 0
    res = ""

    while True:
        try:
            if index == x:
                break
            res += str(my_list[index])
            index += 1
        except IndexError:
            break

    print(res)
    return index


my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list(my_list, 2)
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))
