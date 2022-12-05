override_pairs = 0
with open("input") as list_of_pair_assignments:
    for pair_assignments in list_of_pair_assignments:
        first_pair, second_pair = pair_assignments.split(",")
        first_range = list(
            range(
                int(first_pair.split("-")[0]), int(first_pair.split("-")[1]) + 1
            )
        )
        second_range = list(
            range(
                int(second_pair.split("-")[0]),
                int(second_pair.split("-")[1]) + 1,
            )
        )
        first_check = all(item in first_range for item in second_range)
        second_check = all(item in second_range for item in first_range)
        if first_check or second_check:
            override_pairs = override_pairs + 1
print(override_pairs)
