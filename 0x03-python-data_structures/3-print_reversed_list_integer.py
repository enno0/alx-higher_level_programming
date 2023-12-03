#!/usr/bin/python3
#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    l = len(my_list)
    for i in range(l - 1, -1, -1):
        print("{:d}".format(my_list[i]))
