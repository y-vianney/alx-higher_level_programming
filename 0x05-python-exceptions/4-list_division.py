#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """function that returns a new list (length = list_length)
    with all divisions
    """

    new_list = []

    for _ in range(list_length):
        try:
            new_list.append(my_list_1[_] / my_list_2[_])
        except ZeroDivisionError:
            new_list.append(0)
            print("division by 0")
        except TypeError:
            new_list.append(0)
            print("wrong type")
        except IndexError:
            new_list.append(0)
            print("out of range")
        finally:
            pass

    return new_list
