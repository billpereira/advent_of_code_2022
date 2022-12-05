# [V]     [B]                     [C]
# [C]     [N] [G]         [W]     [P]
# [W]     [C] [Q] [S]     [C]     [M]
# [L]     [W] [B] [Z]     [F] [S] [V]
# [R]     [G] [H] [F] [P] [V] [M] [T]
# [M] [L] [R] [D] [L] [N] [P] [D] [W]
# [F] [Q] [S] [C] [G] [G] [Z] [P] [N]
# [Q] [D] [P] [L] [V] [D] [D] [C] [Z]
#  1   2   3   4   5   6   7   8   9

stacks = [[]]
stacks.append(["Q", "F", "M", "R", "L", "W", "C", "V"])
stacks.append(["D", "Q", "L"])
stacks.append(["P", "S", "R", "G", "W", "C", "N", "B"])
stacks.append(["L", "C", "D", "H", "B", "Q", "G"])
stacks.append(["V", "G", "L", "F", "Z", "S"])
stacks.append(["D", "G", "N", "P"])
stacks.append(["D", "Z", "P", "V", "F", "C", "W"])
stacks.append(["C", "P", "D", "M", "S"])
stacks.append(["Z", "N", "W", "T", "V", "M", "P", "C"])
instructions = []


def print_top_of_stacks(stacks):
    for index, stack in enumerate(stacks):
        print(index, stack[-1:])


def get_instructions_mapped():
    with open("input") as instructions_file:
        for instruction in instructions_file:
            instructions_splitted = instruction.split(" ")
            instructions.append(
                {
                    "move": int(instructions_splitted[1]),
                    "from": int(instructions_splitted[3]),
                    "to": int(instructions_splitted[5].replace("\n", "")),
                }
            )


def perform_movements(movements):
    print(
        f'***\nMoving {movements["move"]} from {movements["from"]} to {movements["to"]}'
    )
    print(f'Original stack {movements["from"]} : {stacks[movements["from"]]}')
    print(f'Original stack {movements["to"]} : {stacks[movements["to"]]}')
    for i in range(movements["move"]):
        element_to_move = stacks[movements["from"]].pop()
        stacks[movements["to"]].append(element_to_move)
    print(f'New stack {movements["from"]} : {stacks[movements["from"]]}')
    print(f'New stack {movements["to"]} : {stacks[movements["to"]]}')


get_instructions_mapped()

for instruction in instructions:
    perform_movements(instruction)

print_top_of_stacks(stacks)
