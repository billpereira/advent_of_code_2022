# Process input
priority_list = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
priority_sum = 0
group_index = 0


def find_intersection(first_compartment, second_compartment):
    common_element = list(
        set(first_compartment).intersection(second_compartment)
    )
    return common_element


with open("input") as rucksack_file:
    for rucksack in rucksack_file:
        if group_index == 0:
            first_rucksack = rucksack
            group_index = group_index + 1
        elif group_index == 1:
            second_rucksack = rucksack
            group_index = group_index + 1
        elif group_index == 2:
            third_rucksack = rucksack
            first_intersection = find_intersection(
                first_rucksack.strip(), second_rucksack.strip()
            )
            common_element = find_intersection(
                first_intersection, third_rucksack
            )
            priority_value = priority_list.index(common_element[0]) + 1
            priority_sum = priority_sum + priority_value
            group_index = 0

print(priority_sum)
