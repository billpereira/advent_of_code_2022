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
with open("input") as rucksack_file:
    for rucksack in rucksack_file:
        # print(len(rucksack.strip()))
        middle_lengh = len(rucksack.strip()) // 2
        first_compartment = rucksack[:middle_lengh]
        second_compartment = rucksack[middle_lengh:]
        common_element = list(
            set(first_compartment).intersection(second_compartment)
        )
        priority_value = priority_list.index(common_element[0]) + 1
        priority_sum = priority_sum + priority_value
        # print(first_compartment, second_compartment)
        print(common_element[0], priority_value, priority_sum)
