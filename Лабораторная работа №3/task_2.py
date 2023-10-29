def find_common_participants(first_string, second_string, separator=','):
    return list(set(first_string.split(separator)).intersection(second_string.split(separator)))


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, '|'))
