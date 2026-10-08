from data import data_cleaner
from group import create_group
from miangin import mian_gin

raw_data = [
    ("Tehran", 32, 40, "1402/05/12"),
    ("Shiraz", 28, 55, "1402/05/12"),
    ("Tehran", 35, 38, "1402/05/13"),
    ("Mashhad", 38, 20, "1402/05/12"),
    ("Mashhad", -39, 25, "1402/05/14"),
    ("Shiraz", 30, 50, "1402/05/13"),
    ("Isfahan", 42, 15, "1402/05/12"),
    ("Tehran", 29, 45, "1402/05/14"),
    ("Mashhad", 40, 18, "1402/05/13"),
    ("Isfahan", 80, 25, "1402/05/14"),
    ("Shiraz", 26, 60, "1402/05/14"),
    ("Rasht", 22, 80, "1402/05/12"),
    ("Tehran", -5, 30, "1402/05/15"),
    ("Mashhad", 36, 25, "1402/05/14"),
    ("Tehran", -40, 25, "1402/05/14")
]

list_clean,list_removes = data_cleaner(raw_data)
group_data = create_group(list_clean)
dict_miangin = mian_gin(group_data)

print(list_removes)