def create_group(lst:list):
    data_dict = {}
    for i in lst:
        if not i[0] in data_dict:
            data_dict[i[0]] = []
            data_dict[i[0]].append(i[1:3])
        else:
            data_dict[i[0]].append(i[1:3])

    return data_dict
