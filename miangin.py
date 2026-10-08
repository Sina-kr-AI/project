def mian_gin(x_dict:dict):
    new_dict = {}

    for i in x_dict:
        n_d = 0
        n_r = 0
        for d,r in x_dict[i]:
            n_d+=d
            n_r+=r
        miangin_d = n_d/len(x_dict[i])
        miangin_r = n_r/len(x_dict[i])
        if not i in new_dict:
            new_dict[i] = {}
            new_dict[i]["miangin dama"] = miangin_d
            new_dict[i]["miangin rotobat"] = miangin_r

    return new_dict




new_dict = {
    "Tehran": {
        "Miangin dama": 34,
        "Miangin rotobat":
    }
}

new_dict["Tehran"][Mi]