#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list is None:
        return None
    else:
        new = []
        for i in my_list:
            if i == search:
                new.append(replace)
            else:
                new.append(i)
        return new
