# Calorie Counting" - Day 1 - Advent of Code 2022
# Initialize variables to keep biggest collectors
elf_index = 0
current_sum = 0
biggest_elf = 0
biggest_sum = 0
second_biggest_elf = 0
second_biggest_sum = 0
third_biggest_elf = 0
third_biggest_sum = 0

# Process input
with open("elfs_input") as calory_file:
    for star in calory_file:
        if star == "\n":
            if current_sum >= biggest_sum:
                third_biggest_elf = second_biggest_elf
                second_biggest_elf = biggest_elf
                biggest_elf = elf_index
                third_biggest_sum = second_biggest_sum
                second_biggest_sum = biggest_sum
                biggest_sum = current_sum
            else:
                if current_sum >= second_biggest_sum:
                    third_biggest_elf = second_biggest_elf
                    second_biggest_elf = elf_index
                    third_biggest_sum = second_biggest_sum
                    second_biggest_sum = current_sum
                else:
                    if current_sum >= third_biggest_sum:
                        third_biggest_elf = elf_index
                        third_biggest_sum = current_sum

            elf_index = elf_index + 1
            current_sum = 0
        else:
            current_sum = current_sum + int(star.replace("\n", ""))

        status = f"""
        1 colocado: {biggest_elf} Soma total: {biggest_sum}
        2 colocado: {second_biggest_elf} Soma total: {second_biggest_sum}
        3 colocado: {third_biggest_elf} Soma total: {third_biggest_sum}
        Total dos 3 elfos: {biggest_sum+second_biggest_sum+third_biggest_sum}
        """

print(status)
