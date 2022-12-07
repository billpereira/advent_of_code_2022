folder_structure = {}
all_folder_size = {}
current_folder = []


def update_current_folder(command, directory):
    if command == "cd":
        if directory == "..":
            current_folder.pop()
        elif directory == "/":
            current_folder.append(directory)
            if "".join(current_folder) not in folder_structure.keys():
                folder_structure["".join(current_folder)] = []
        else:
            current_folder.append(directory + "/")
            if "".join(current_folder) not in folder_structure.keys():
                folder_structure["".join(current_folder)] = []


def update_on_listing(item, size=""):
    if size == "":
        folder_structure["".join(current_folder)].append(
            "".join(current_folder) + item + "/"
        )
    else:
        folder_structure["".join(current_folder)].append((item, int(size)))


def calculate_size_current_folder(folder_path):
    current_sum_of_path = 0
    for item in folder_structure[folder_path]:
        if isinstance(item, tuple):
            current_sum_of_path = current_sum_of_path + item[1]
        else:
            current_sum_of_path = (
                current_sum_of_path + calculate_size_current_folder(item)
            )
    return current_sum_of_path


def calculate_total_size_of_folders():
    all_folder_size = {}

    for folder in folder_structure.keys():
        all_folder_size[folder] = calculate_size_current_folder(folder)

    total_file_system = 70000000
    total_used_space = all_folder_size["/"]
    total_available = total_file_system - total_used_space
    total_needed = 30000000 - total_available
    smallest_needed_to_delete = total_file_system
    path_to_delete = ""

    for item in all_folder_size:
        if all_folder_size[item] >= total_needed:
            if all_folder_size[item] <= smallest_needed_to_delete:
                smallest_needed_to_delete = all_folder_size[item]
                path_to_delete = item

    print("available: ", total_available)
    print("needed:", total_needed)
    print("used:", total_used_space)
    print("Path to delete:", path_to_delete)
    print("Amount:", smallest_needed_to_delete)


def proccess_line(line):
    arguments = line.replace("\n", "").split(" ")
    if arguments[0] == "$":
        if arguments[1] == "cd":
            directory = arguments[2]
            update_current_folder(arguments[1], directory)
    else:
        if arguments[0] == "dir":
            update_on_listing(arguments[1])
        else:
            update_on_listing(
                arguments[1],
                arguments[0],
            )


def main():
    with open("small_input") as commands_input:
        for line in commands_input:
            proccess_line(line)
    print(folder_structure)
    calculate_total_size_of_folders()


main()
