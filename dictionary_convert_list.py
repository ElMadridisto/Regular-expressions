def dict_conv_list(dict):
    list_off = []
    for key, value in dict.items():
        for items in [key, value]:
            if type(items) is str:
                list_1 = items.split(',')
            else:
                list_1.extend(items)
        list_off.append(list_1)
    return list_off