my_list = [0, 17, 12, 1, 6, 47, 23, 39, 26, 37, 41, 8]

this_list = []

this_list.append(my_list.pop(-2))
this_list.append(my_list.pop(4))
this_list.append(my_list.pop(-6))
this_list.append(my_list.pop(3))
this_list.append(my_list.pop(5))
this_list.append(my_list.pop(-1))
this_list.insert(0, 72)
this_list.append(24)


print(this_list)