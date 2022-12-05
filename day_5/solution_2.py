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


def print_top_of_stacks(stacks):
    for index, stack in enumerate(stacks):
        print(index, stack[-1:])


def perform_movements():
    with open("input") as instructions_file:
        for instructions in instructions_file:
            amount_to_move = int(instructions.split(" ")[1])
            from_stack = int(instructions.split(" ")[3])
            to_stack = int(instructions.split(" ")[5])
            print(
                f"***\nMoving {amount_to_move} from {from_stack} to {to_stack}"
            )
            print(f"Original stack {from_stack} : {stacks[from_stack]}")
            print(f"Original stack {to_stack} : {stacks[to_stack]}")
            elements_to_move = stacks[from_stack][-amount_to_move:]
            del stacks[from_stack][-amount_to_move:]
            stacks[to_stack].extend(elements_to_move)
            print(f"New stack {from_stack} : {stacks[from_stack]}")
            print(f"New stack {to_stack} : {stacks[to_stack]}")


def main():
    perform_movements()
    print_top_of_stacks(stacks)


main()
