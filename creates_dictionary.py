def create_dict(list):
    dict_new = {}
    for item in list:
        item = item.split(",")
        if (item[0] + ',' + item[1]) not in dict_new:
            dict_new.update({item.pop(0) + ',' + item.pop(0): item})
        else:
            for item_2 in dict_new[item[0] + ',' + item[1]]:
                if item_2 == '':
                    i = dict_new[item[0] + ',' + item[1]].index(item_2)
                    dict_new[item[0] + ',' + item[1]][i] = item[i + 2]
    return dict_new