input_file = open("input", "r")
strategy_lines = input_file.readlines()
current_sum = 0
own_shapes_value = {"Y": 2, "X": 1, "Z": 3}
loose_table = {"A": "Z", "B": "X", "C": "Y"}
drawn_table = {"A": "X", "B": "Y", "C": "Z"}
win_table = {"A": "Y", "B": "Z", "C": "X"}

for matches in strategy_lines:
    match_value = matches.replace("\n", "").split(" ")
    if match_value[1] == "X":
        result_value = 0
        current_score = (
            result_value + own_shapes_value[loose_table[match_value[0]]]
        )
    if match_value[1] == "Y":
        result_value = 3
        current_score = (
            result_value + own_shapes_value[drawn_table[match_value[0]]]
        )
    if match_value[1] == "Z":
        result_value = 6
        current_score = (
            result_value + own_shapes_value[win_table[match_value[0]]]
        )
    current_sum = current_sum + current_score
print(current_sum)
