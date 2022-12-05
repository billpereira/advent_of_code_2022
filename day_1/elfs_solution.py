# Read input
input_file = open("elfs_input", "r")
calory_lines = input_file.readlines()
elf_index = 0
current_sum = 0
choosen_elf = 0
biggest_sum = 0

for star in calory_lines:
    if star == "\n":
        if current_sum >= biggest_sum:
            biggest_sum = current_sum
            choosen_elf = elf_index
        elf_index = elf_index + 1
        current_sum = 0
    else:
        current_sum = current_sum + int(star.replace("\n", ""))

    print(
        f"The elf {elf_index} has {current_sum} while the elf with more calories is {choosen_elf} with {biggest_sum} calories"
    )

# find the biggest sum
# biggest sum = 0
# sum till blank increment position verify if biggest
