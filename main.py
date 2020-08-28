from colorama import Fore
from collections import Counter


def most_frequent(List):
    occurence_count = Counter(List)
    return [line[0] for line in occurence_count.most_common(2)]


def remove_date(line):
    if "Today" in line:
        name_line = line.split("Today")
        name_line[1] = ""
    elif "Yesterday" in line:
        name_line = line.split("Yesterday")
        name_line[1] = ""
    elif "/" in line:
        name_line = [line[:-11], ""]
    else:
        return line
    return name_line


message = open("message.txt", "r")

seperate_message = message.readlines()

for line in seperate_message:
    current_line = remove_date(line)
    if len(current_line) == 2:
        for line in current_line:
            print(f"{Fore.GREEN}{line}")
    else:
        print(f"{Fore.RESET}{str(line)}")
