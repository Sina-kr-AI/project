def data_cleaner(lst:list):
    lst_new = []
    lst_remove = []
    for tople in lst:
        if tople[1]>=50 or tople[1]<=-20:
            lst_remove.append(tople)
        else:
            lst_new.append(tople)

    return lst_new,lst_remove