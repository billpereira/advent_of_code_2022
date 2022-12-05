input_file = open("input", "r")
strategy_lines = input_file.readlines()
current_sum = 0
own_shapes_value = {"Y": 2, "X": 1, "Z": 3}


for matches in strategy_lines:
    match_value = matches.replace("\n", "").split(" ")
    if (
        (match_value[1] == "X" and match_value[0] == "A")
        or (match_value[1] == "Y" and match_value[0] == "B")
        or (match_value[1] == "Z" and match_value[0] == "C")
    ):
        result_value = 3
    if (
        (match_value[1] == "Y" and match_value[0] == "A")
        or (match_value[1] == "Z" and match_value[0] == "B")
        or (match_value[1] == "X" and match_value[0] == "C")
    ):
        result_value = 6
    if (
        (match_value[1] == "X" and match_value[0] == "B")
        or (match_value[1] == "Y" and match_value[0] == "C")
        or (match_value[1] == "Z" and match_value[0] == "A")
    ):
        result_value = 0
    current_score = own_shapes_value[match_value[1]] + result_value
    current_sum = current_sum + current_score

print(current_sum)
