/* REXX */
/* Calorie Counting - Day 1 - Advent of Code 2022 */
elf_index = 0
current_sum = 0
biggest_elf = 0
biggest_sum = 0
second_biggest_elf = 0
second_biggest_sum = 0
third_biggest_elf = 0
third_biggest_sum = 0

INPUT_DSN='Z93415.ADVCODE.INPUT(DAY1)'

ADDRESS TSO
"ALLOC F(INPUTDD) DA('"||INPUT_DSN||"') SHR"
"EXECIO * DISKR INPUTDD (FINIS STEM STAR."

DO i = 1 to STAR.0
    if word(STAR.i,1) == '' then
    do
        elf_index = elf_index + 1
        if current_sum >= biggest_sum then 
        do
            third_biggest_elf = second_biggest_elf
            second_biggest_elf = biggest_elf
            biggest_elf = elf_index
            third_biggest_sum = second_biggest_sum
            second_biggest_sum = biggest_sum
            biggest_sum = current_sum
        end
        else do 
            if current_sum >= second_biggest_sum then
            do
                third_biggest_elf = second_biggest_elf
                second_biggest_elf = elf_index
                third_biggest_sum = second_biggest_sum
                second_biggest_sum = current_sum
            end
            else do
                if current_sum >= third_biggest_sum then
                do
                    third_biggest_elf = elf_index
                    third_biggest_sum = current_sum
                end
            end
        end
        current_sum = 0
    end
    else do
        star_calories = STAR.i
        current_sum = current_sum + star_calories
    end
END
"FREE F(INPUTDD)"

total = biggest_sum+second_biggest_sum+third_biggest_sum
say "1 colocado: " biggest_elf " Soma total: " biggest_sum
say "2 colocado: " second_biggest_elf " Soma total: " second_biggest_sum
say "3 colocado: " third_biggest_elf " Soma total: " third_biggest_sum
say "Total dos 3 elfos: " total

